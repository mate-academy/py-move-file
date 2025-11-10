import os
import shutil


def move_file(command: str) -> None:
    result = command.strip().split()
    if len(result) != 3 or result[0] != "mv":
        raise ValueError

    src = result[1]
    dst = result[2]

    if dst.endswith("/"):
        dst = os.path.join(dst, os.path.basename(src))

    dst_dir = os.path.dirname(dst)
    if dst_dir:
        os.makedirs(dst_dir, exist_ok=True)

    shutil.copy2(src, dst)
    os.remove(src)
