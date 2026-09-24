import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    source = parts[1]
    dest = parts[2]

    # If destination ends with /, it's a directory - append filename
    if dest.endswith("/"):
        dest = dest + os.path.basename(source)

    # Create all necessary directories
    dest_dir = os.path.dirname(dest)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    # Move the file (copies and removes original)
    shutil.move(source, dest)
