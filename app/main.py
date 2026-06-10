import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, src, dst = parts

    if dst.endswith("/"):
        _create_dirs(dst)
        dst = os.path.join(dst, os.path.basename(src))
    else:
        parent_dir = os.path.dirname(dst)
        if parent_dir:
            _create_dirs(parent_dir)

    shutil.copy2(src, dst)
    os.remove(src)


def _create_dirs(path: str) -> None:
    parts = path.replace("\\", "/").split("/")
    current = ""

    for part in parts:
        if not part:
            continue
        current = os.path.join(current, part)
        if not os.path.exists(current):
            os.mkdir(current)
