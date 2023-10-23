import os
import shutil


def move_file(command: str) -> None:
    tag, source, destination = command.split()
    if len(destination.split("/")) == 1:
        os.rename(source, destination)
        return
    split_path = destination.split("/")
    folder_path = split_path[:-1]
    new_name = split_path[-1]
    path = "/".join(folder_path)
    os.makedirs(path, exist_ok=True)
    os.rename(source, new_name)
    shutil.move(new_name, path)
