import os


def move_file(command: str) -> None:
    _, source, destination = command.split()

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    dirname = os.path.dirname(destination)
    if dirname:
        os.makedirs(dirname, exist_ok=True)

    os.rename(source, destination)
