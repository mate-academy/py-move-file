import os
import shutil


def move_file(command: str) -> None:
    parts = command.split(" ")

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, destination = parts

    dir_name = os.path.dirname(destination)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)

    shutil.move(source, destination)
