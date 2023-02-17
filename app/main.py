import os
import shutil


def move_file(command: str) -> None:
    command, file_to_opening, path_to_file = command.split()

    if command == "mv":
        if path_to_file.count("/"):
            path_to_writing = os.path.split(path_to_file)
            os.makedirs(os.path.join(*path_to_writing[0:-1]))
            shutil.copyfile(file_to_opening, os.path.join(*path_to_writing))
            os.remove(file_to_opening)
        else:
            os.rename(file_to_opening, path_to_file)
