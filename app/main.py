import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, destination = parts

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    dirname = os.path.dirname(destination)
    if dirname:
        path = ""
        for part in dirname.split("/"):
            path = os.path.join(path, part)
            if not os.path.exists(path):
                os.mkdir(path)

    shutil.copy(source, destination)
    os.remove(source)
