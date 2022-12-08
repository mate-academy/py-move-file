import os
import shutil


def move_file(command: str) -> None:

    if "/" in command and command.split()[0] == "mv":
        list_command = command.split()
        list_path_to = command.split()[2].split("/")

        upd_path_str = ""
        for folder in list_path_to:
            upd_path_str += folder + "/"
            if upd_path_str[-4::] != "txt/":
                os.mkdir(upd_path_str)

        with (open(list_command[1], "r") as file_in,
              open(list_command[2], "a") as file_out):
            shutil.copyfile(file_in.name, file_out.name)

        os.remove(file_in.name)

    if "/" not in command and len(command.split()) == 3\
            and command.split()[0] == "mv":
        os.rename(command.split()[1], command.split()[2])
