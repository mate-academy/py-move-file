import os
from shutil import move


def move_file(command: str) -> None:
    if "/" not in command:
        _, old_name, new_name = command.split(" ")
        os.rename(old_name, new_name)
        return

    _, source_file, path = command.split(" ")
    new_file = path.split("/")[-1]
    path = path.replace(new_file, "")

    try:
        os.makedirs(path)
    except FileExistsError:
        print("The directory already exists: ", path)

    move(source_file, path + new_file)
