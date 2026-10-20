import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. Expected: mv <src> <dest>")

    _, src, dest = parts

    if dest.endswith("/"):
        dest = os.path.join(dest, os.path.basename(src))

    dest_dir = os.path.dirname(dest)
    if dest_dir:
        current = ""
        for part in dest_dir.replace("\\", "/").split("/"):
            if part:
                current = os.path.join(current, part) if current else part
                if not os.path.exists(current):
                    os.mkdir(current)

    shutil.copy2(src, dest)
    os.remove(src)
