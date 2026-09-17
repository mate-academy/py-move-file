import os
import shutil


def move_file(command: str) -> None:
    command = command.split(" ")
    filename = command[1]
    directory = command[2].split("/")
    new_filename = directory.pop(-1)
    if not new_filename:
        new_filename = filename
    if directory:
        destination = "/".join(directory + [new_filename])
        path_to_create = "/".join(directory)
        if os.path.isfile(path_to_create):
            os.remove(path_to_create)
        os.makedirs(path_to_create, exist_ok=True)
    else:
        destination = new_filename
        if os.path.isdir(destination):
            destination = os.path.join(destination, filename)
    if os.path.isdir(destination):
        destination = os.path.join(destination, filename)
    if os.path.isfile(destination):
        os.remove(destination)
    shutil.move(filename, destination)
