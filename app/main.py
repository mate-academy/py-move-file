import os


def move_file(command: str) -> None:
    source, destination = read_command(command)
    create_path_to(destination)

    with (open(source, "r") as target_file,
          open(destination, "w") as destination_file):
        destination_file.write(target_file.read())

    os.remove(source)


def read_command(command: str) -> tuple[str, str]:
    command_items = command.split()

    try:
        verify_command(command_items)
    except (ValueError, FileNotFoundError):
        raise

    return command_items[1], command_items[-1]


def create_path_to(path: str) -> None:
    head = os.path.split(path)[0]

    if head != "" and not os.path.isdir(head):
        os.makedirs(head)


def verify_command(command: list[str]) -> None:
    if not command:
        raise ValueError("No command has been given.")
    if command[0] != "mv":
        raise ValueError("Command must start with 'mv' keyword.")
    if len(command) <= 1:
        raise ValueError("No file arguments has been given.")
    if len(command) > 3:
        raise ValueError("Excessive file arguments has been given.")
    if command[1] == command[-1]:
        raise ValueError("Target and destination are equal.")
    if not os.path.isfile(command[1]):
        raise FileNotFoundError("Source file does not exist.")
