import os
import shutil


def move_file(command: str) -> None:
    command, source, destination = command.split()
    if command != "mv":
        return
    path_, new_file_name = os.path.split(destination)
    if path_ and not os.path.exists(path_):
        os.makedirs(path_)
    shutil.move(source, destination)
