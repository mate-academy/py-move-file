import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    _, src, dest = parts

    if dest.endswith(os.sep) or os.path.isdir(dest):
        dest = os.path.join(dest, os.path.basename(src))

    dest_dir = os.path.dirname(dest)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    if os.path.exists(src):
        shutil.copy(src, dest)
        os.remove(src)
