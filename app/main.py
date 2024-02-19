import os
import shutil


def move_file(command: str) -> None:
    command = command.split()
    if len(command) != 3 or command[0] != "mv":
        raise Exception(
            "Invalid command; must be format: <mv> <source_file> <destination>"
        )
    _, source, destination = command
    directory = os.path.dirname(destination)
    if directory:
        os.makedirs(directory, exist_ok=True)
    shutil.move(source, destination)
