import os
import shutil


def move_file(command: str) -> None:

    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError

    source_file = parts[1]
    destination = parts[2]

    if not os.path.isfile(source_file):
        raise FileNotFoundError

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source_file))
    else:
        dest_dir = os.path.dirname(destination)
        if dest_dir:
            os.makedirs(dest_dir, exist_ok=True)

    shutil.move(source_file, destination)
