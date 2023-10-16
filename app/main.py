import os
import shutil
from shutil import move


def move_file(command: str) -> None:
    command_list = command.split(" ")

    flag = command_list[0]
    file_name = command_list[1]
    move_to = command_list[2]

    if flag == "mv":
        dirs = os.path.dirname(move_to)
        if dirs:
            os.makedirs(dirs, exist_ok=True)
        os.replace(file_name, move_to)

