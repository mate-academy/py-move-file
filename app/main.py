import os
import shutil


def move_file(command: str) -> None:
    parts = command.strip().split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. Use: mv source destination")

    src, dest = parts[1], parts[2]

    if not os.path.isfile(src):
        raise FileNotFoundError(f"Source file \"{src}\" not found.")

    if dest.endswith("/"):
        os.makedirs(dest, exist_ok=True)
        dest = os.path.join(dest, os.path.basename(src))
    else:
        dest_dir = os.path.dirname(dest)
        if dest_dir:
            os.makedirs(dest_dir, exist_ok=True)

    shutil.move(src, dest)
