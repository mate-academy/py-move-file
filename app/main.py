import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "mv":
        return

    _, source, destination = command_parts
    directory = os.path.dirname(destination)
    if directory:
        os.makedirs(directory, exist_ok=True)
    os.replace(source, destination)
