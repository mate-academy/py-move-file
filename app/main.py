import os
import shutil


def move_file(command: str) -> None:
    if (command[:3]) != "mv " or command.count(" ") != 2:
        return
    _, old_file, new_file = command.split(" ")

    if new_file.count("/") != 0:
        *path, new_file_name = new_file.split("/")
        print(path)
        new_path = os.path.join(*path)
        if not os.path.isdir(new_path):
            os.makedirs(new_path)

        new_file = os.path.join(new_path, new_file_name)
    shutil.move(old_file, new_file)
