import os
import shutil


def move_file(command: str) -> None:
    _, source, destination = command.split()
    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        parent_dir = os.path.dirname(destination)
        if parent_dir and not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
    shutil.move(source, destination)
