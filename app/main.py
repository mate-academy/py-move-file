import os
from pathlib import Path


def move_file(command: str) -> None:
    command_part = command.split()

    if len(command_part) != 3 or command_part[0] != "mv":
        return

    _, source, destination = command_part

    with open(source, "r") as src_file:
        dir_path = Path(destination).parent

        if str(dir_path) != ".":
            os.makedirs(dir_path, exist_ok=True)

        with open(destination, "w") as dst_file:
            dst_file.write(src_file.read())

    os.remove(source)
