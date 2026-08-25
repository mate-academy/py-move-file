import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return
    _, source, destination = parts

    filename = os.path.basename(source)

    if destination.endswith("/"):
        destination = os.path.join(destination, filename)
    dir_path = os.path.dirname(destination)
    if dir_path:
        parts_dir = dir_path.split("/")
        for i in range(len(parts_dir)):
            path = "/".join(parts_dir[:i + 1])
            if not os.path.isdir(path):
                os.mkdir(path)

    shutil.copy(source, destination)
    os.remove(source)
