import os
import shutil


def move_file(command: str) -> None:
    _, current_file, new_file_path = command.split()
    dir_list = new_file_path.split("/")
    new_file_name = dir_list.pop()
    new_dir = ""

    for directory in dir_list:
        if not os.path.exists(new_dir + directory):
            os.mkdir(new_dir + directory)
        new_dir += directory + "/"
    shutil.copy(current_file, new_dir + new_file_name)
    os.remove(current_file)
