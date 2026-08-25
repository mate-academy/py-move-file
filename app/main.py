import os
import shutil


def move_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format")

    _, src, dest = parts

    if dest.endswith("/"):
        dest = os.path.join(dest, os.path.basename(src))

    dest_dir = os.path.dirname(dest)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    shutil.copy2(src, dest)
    os.remove(src)
