import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    source = parts[1]
    destination = parts[2]

    if not os.path.exists(source):
        return

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    dest_dir = os.path.dirname(destination)

    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    shutil.move(source, destination)
