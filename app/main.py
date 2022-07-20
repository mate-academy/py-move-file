import os


def move_file(command: str):
    ls_from_command = command.split()
    path_and_name = ls_from_command[2].rsplit("/", 1)
    file = open(ls_from_command[1], "r").readlines()
    if len(path_and_name) == 1:
        os.rename(ls_from_command[1], ls_from_command[2])
    if len(path_and_name) > 1:
        os.makedirs(path_and_name[0])
        with os.popen(ls_from_command[2], "w") as new_f:
            new_f.writelines(file)
            os.remove(ls_from_command[1])
