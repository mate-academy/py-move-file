import os


def move_file(command: str) -> None:
    parts = command.split()

    source = parts[1]
    destination = parts[2]

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        directory = os.path.dirname(destination)
        if directory:
            os.makedirs(directory, exist_ok=True)

    os.rename(source, destination)
