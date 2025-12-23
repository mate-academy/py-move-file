import os
import shutil


def move_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    _, src, dst = parts

    if dst.endswith("/"):
        dst_dir = dst.rstrip("/")
        os.makedirs(dst_dir, exist_ok=True)
        dst_path = os.path.join(dst_dir, os.path.basename(src))
    else:
        dst_dir = os.path.dirname(dst)
        if dst_dir:
            os.makedirs(dst_dir, exist_ok=True)
        dst_path = dst

    if os.path.exists(dst_path):
        os.remove(dst_path)

    shutil.copy(src, dst_path)
    os.remove(src)
