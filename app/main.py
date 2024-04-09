import os


def move_file(command: str) -> None:

    command_parts = command.split()
    if not len(command_parts) == 3 and command_parts[0] == "mv":
        raise Exception(f"Entered incorrect command {command}")

    with open(command_parts[1], "r") as main_file:
        content_of_file = main_file.read()
    dir_path, _ = os.path.split(command_parts[2])
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
    with open(command_parts[2], "w") as copied_file:
        copied_file.write(content_of_file)
        os.remove(command_parts[1])
