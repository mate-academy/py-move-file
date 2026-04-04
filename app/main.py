import os
import shutil


def move_file(command: str):
    command_spl = command.replace(" ", "/")
    elems = command_spl.split("/")

    file = elems[1]
    file_new = elems[-1]
    destin_dir_str = "/".join(elems[2:-1])

    os.makedirs(destin_dir_str)
    shutil.move(file, os.path.join(destin_dir_str, file_new))
