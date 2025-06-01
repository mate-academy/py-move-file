import os
import shutil


def move_file(command: str) -> None:
    text = command.split()

    if text[0] != "mv" or len(text) != 3:
        return

    source = text[1]
    destination = text[2]

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        filename = os.path.basename(source)
        destination = os.path.join(destination, filename)
    else:
        dir_path = os.path.dirname(destination)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

    shutil.move(source, destination)
