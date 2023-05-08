import os


def move_file(command: str) -> None:
    if len(command.split()) != 3 or command.split()[0] != "mv":
        return

    _, source, destination = command.split()
    directory = os.path.dirname(destination)
    if directory:
        os.makedirs(directory, exist_ok=True)
    os.replace(source, destination)
