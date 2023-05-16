import os
import shutil


def move_file(command: str) -> None:
    split_command = command.split()
    exist_file, new_name = split_command[1], split_command[2]

    directories = split_command[-1].split("/")
    new_file = directories[-1]

    src_file = os.getcwd() + "\\" + exist_file
    last_dir = "\\".join(directories[:-2])
    parent_dir = os.getcwd() + "\\" + last_dir

    if len(directories) == 1:
        return os.rename(exist_file, new_name)

    dst_file1 = parent_dir + "\\" + directories[-2] + "\\" + exist_file
    dst_file2 = parent_dir + "\\" + directories[-2] + "\\" + new_file

    path = os.getcwd()
    for directorie in directories[:-1]:
        path += "\\" + directorie
    if os.path.exists(path):

        shutil.copy(src_file, dst_file1)

        os.remove(exist_file)
        return os.rename(dst_file1, dst_file2)

    path = os.path.join(parent_dir, directories[-2])
    os.makedirs(path)

    shutil.copy(src_file, dst_file1)

    os.remove(exist_file)
    os.rename(dst_file1, dst_file2)
