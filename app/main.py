import os
import shutil


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        mv, source, destination = command.split()
        directory = os.path.dirname(destination)
        new_destination = os.path.join(
            directory, os.path.basename(destination)
        )
        if mv == "mv":
            if directory:
                os.makedirs(directory, exist_ok=True)

            shutil.move(source, new_destination)
