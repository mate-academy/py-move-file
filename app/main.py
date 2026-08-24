import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    source: str = parts[1]
    destination: str = parts[2]
    if destination.endswith('/'):
        destination = os.path.join(destination, os.path.basename(source))
    dest_dir = os.path.dirname(destination)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    shutil.move(source, destination)
