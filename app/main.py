import os
import shutil


def move_file(command: str) -> None:
    mv, source, destination = command.split()
    directory = os.path.dirname(destination)
    new_destination = os.path.join(directory, os.path.basename(destination))
    if mv == "mv":
        if not destination.count("/"):
            if os.path.exists(destination):
                os.remove(destination)
            os.rename(source, destination)
        else:
            os.makedirs(directory, exist_ok=True)
            shutil.move(source, new_destination)
