import os
import shutil


def move_file(command: str) -> None:
    _, source, destination = command.split()
    directory = os.path.dirname(destination)
    if directory:
        os.makedirs(directory, exist_ok=True)
    shutil.move(source, destination)
