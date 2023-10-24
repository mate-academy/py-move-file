import os
import shutil


def move_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) != 3:
        return
    tag, source, destination = command_split
    directory, filename = os.path.split(destination)
    if not directory:
        os.rename(source, destination)
        return
    os.makedirs(directory, exist_ok=True)
    os.rename(source, filename)
    shutil.move(filename, directory)
