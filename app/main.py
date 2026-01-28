from os import path, makedirs
from shutil import move


def move_file(command: str) -> None:
    _, source, destination = command.split()

    if (not (command.startswith("mv "))
            or not (source.endswith(".txt"))
            or not (destination.endswith(".txt"))):
        return

    if not (path.dirname(destination) == ""):
        makedirs(path.dirname(destination), exist_ok=True)
    move(source, destination)
