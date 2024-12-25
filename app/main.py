from distutils.file_util import copy_file
import os


def move_file(command: str) -> None:
    if (command[:3]) != "mv " or command.count(" ") != 2:
        return
    _, old_file, new_file = command.split(" ")

    if new_file.count("/") != 0:
        path = ""
        for i in new_file.split("/"):
            if "." not in i:
                path += i + "/"
                if not os.path.isdir(path):
                    os.mkdir(path)
            else:
                path += i
            new_file = path

    copy_file(old_file, new_file)
    os.remove(old_file)
