import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    source = parts[1]
    destination = parts[2]
    filename = os.path.basename(source)
    if destination.endswith("/"):
        destination = destination + filename

    dir_path = os.path.dirname(destination)

    if dir_path:
        if os.path.isfile(dir_path):
            os.remove(dir_path)
        os.makedirs(dir_path, exist_ok=True)

    shutil.move(source, destination)
