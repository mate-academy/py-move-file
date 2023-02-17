import os
import shutil


def move_file(command: str) -> None:
    command, file_to_opening, path = command.split(" ")
    if command == "mv":
        if path.count("/"):
            path_to_writing = path.split("/")
            os.makedirs(os.path.join(*path_to_writing[0:-1]))
            shutil.copyfile(file_to_opening, os.path.join(*path_to_writing))
            os.remove(file_to_opening)
        else:
            shutil.copyfile(file_to_opening, path)
            os.remove(file_to_opening)
