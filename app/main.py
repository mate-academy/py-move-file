import os
import shutil


def move_file(command: str) -> None:

    if "/" in command:
        list_command = command.split()
        list_path_to = command.split()[2].split("/")

        upd_path_str = ""
        for folder in list_path_to:
            upd_path_str += folder + "/"
            if upd_path_str[-4::] != "txt/":
                os.mkdir(upd_path_str)

        with open(list_command[1], "r"), open(list_command[2], "a"):
            shutil.copyfile(list_command[1], list_command[-1])

        os.remove(list_command[1])
