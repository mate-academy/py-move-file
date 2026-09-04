import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, dest = parts

    if dest.endswith("/"):
        dest = os.path.join(dest, os.path.basename(source))

    directory = os.path.dirname(dest)

    if directory:
        os.makedirs(directory, exist_ok=True)

    shutil.move(source, dest)
