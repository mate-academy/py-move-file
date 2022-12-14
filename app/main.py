import os
import shutil


def move_file(command: str):
    file_name = command.split()[1]
    path = command.split()[2]
    new_file = ""
    parent_dir = os.getcwd()
    if "/" in path:
        path_list = path.split("/")
        new_file += path_list[-1]
        path_list.remove(path_list[-1])
        new_path = "/".join(path_list)
        path_to_file = os.path.join(parent_dir, new_path)
        os.makedirs(path_to_file)
        os.chdir(path_to_file)
    path_to_old_file = os.path.join(parent_dir, file_name)
    shutil.copyfile(path_to_old_file, new_file)
    os.remove(path_to_old_file)
