import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. Use: mv source destination")

    src = parts[1]
    dest = parts[2]

    if not os.path.isfile(src):
        raise FileNotFoundError(f"No such file: '{src}'")

    if dest.endswith("/"):
        dest_dir = dest
        dest_file = os.path.join(dest_dir, os.path.basename(src))
    else:
        dest_dir = os.path.dirname(dest)
        dest_file = dest

    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    shutil.move(src, dest_file)
