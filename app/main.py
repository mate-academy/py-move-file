import os
import shutil


def move_file(command: str) -> None:
    _, src, dst = command.strip().split()

    if not os.path.isfile(src):
        raise FileNotFoundError(f"Source file '{src}' does not exist")

    if dst.endswith("/"):
        os.makedirs(dst, exist_ok=True)
        filename = os.path.basename(src)
        final_dst = os.path.join(dst, filename)
    else:
        dir_path = os.path.dirname(dst)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
        final_dst = dst

    shutil.move(src, final_dst)
