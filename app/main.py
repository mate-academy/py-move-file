import os
from os import mkdir


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return

    if parts[0] != "mv":
        return

    _, src, destination_path = parts

    if not os.path.exists(src):
        return

    if destination_path.endswith(os.sep):
        destination_path = os.path.join(
            destination_path,
            os.path.basename(src)
        )

    dir_path = os.path.dirname(destination_path)
    if dir_path:
        current = ""
        for folder in dir_path.split(os.sep):
            current = os.path.join(current, folder)
            if not os.path.exists(current):
                mkdir(current)

    with open(src, "r") as f_src, open(destination_path, "w") as f_dst:
        f_dst.write(f_src.read())

    os.remove(src)