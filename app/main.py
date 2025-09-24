import os
import shutil


def move_file(command: str) -> None:
    parts = command.strip().split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command. Expected format: "
                         "mv source destination")

    src, dest = parts[1], parts[2]

    dest_dir = os.path.dirname(dest)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    shutil.move(src, dest)
