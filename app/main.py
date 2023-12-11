import os
import shutil
from pathlib import Path


def move_file(command: str) -> None | str:
    command, source_file_name, path_second_file = command.split()

    if command != "mv":
        return "command error"

    path_arr = path_second_file.split("/")
    if len(path_arr) == 1:
        os.rename("./" + source_file_name, "./" + path_arr[0])
    else:
        aim_file_name = path_arr.pop()
        path_arr = path_second_file.split("/")[:-1]
        path = "./" + "/".join(path_arr)
        if Path(path).exists():
            shutil.move(fr"./{source_file_name}", fr"{path}/{aim_file_name}")
        else:
            os.makedirs(path)
            shutil.move(fr"./{source_file_name}", fr"{path}/{aim_file_name}")
