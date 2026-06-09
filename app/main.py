import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, src, dst = parts

    if dst.endswith("/"):
        os.makedirs(dst, exist_ok=True)
        dst = os.path.join(dst, os.path.basename(src))
    else:
        parent_dir = os.path.dirname(dst)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)

    shutil.copy2(src, dst)
    os.remove(src)
