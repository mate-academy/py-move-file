import os
import shutil


def move_file(input_command: str) -> None:
    command, file_to_opening, path_to_file = input_command.split()

    if command == "mv":

        if path_to_file.count("/"):
            os.makedirs(os.path.join(os.path.split(path_to_file)[0]))
            shutil.copyfile(file_to_opening, os.path.join(path_to_file))
            os.remove(file_to_opening)
        else:
            os.rename(file_to_opening, path_to_file)
