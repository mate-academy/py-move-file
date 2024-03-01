import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) != 3 or command[0] != "mv":
        raise ValueError("Invalid command")
    mv_command, source, destination_path = command
    directory = os.path.dirname(destination_path)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with (
        open(source, "r") as source_file,
        open(destination_path, "w") as destination_file
    ):
        destination_file.write(source_file.read())

    os.remove(source)
