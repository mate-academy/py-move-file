import os
import shutil


def move_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. Use: mv source destination")

    src = parts[1]
    dst = parts[2]

    if not os.path.isfile(src):
        raise FileNotFoundError(f"Source file '{src}' does not exist")

    if dst.endswith("/"):
        raise ValueError("Destination must be a file path,"
                         " not a directory ending with '/'")

    dst_dir = os.path.dirname(dst)
    if dst_dir:
        os.makedirs(dst_dir, exist_ok=True)

    shutil.copy2(src, dst)
    os.remove(src)
