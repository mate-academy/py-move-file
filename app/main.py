import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Command must look like: mv source destination")

    _, source, destination = parts

    if destination.endswith("/"):
        destination = destination + os.path.basename(source)

    directory = os.path.dirname(destination)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(source, "rb") as src, open(destination, "wb") as dst:
        dst.write(src.read())

    os.remove(source)
