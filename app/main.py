import os
import shutil


def move_file(command: str) -> None:
    command_list = command.split()
    command_list[2] = command_list[2].split("/")
    new_dir = ""

    for index in range(len(command_list[2]) - 1):
        if not os.path.exists(new_dir + command_list[2][index]):
            os.mkdir(new_dir + command_list[2][index])
        new_dir += command_list[2][index] + "/"
    shutil.copy(command_list[1], new_dir + command_list[2][-1])
    os.remove(command_list[1])
