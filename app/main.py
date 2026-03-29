import os
import shutil


def move_file(command: str) -> None:
    command_list = command.split()
    make_file = command_list[0]
    old_name = command_list[1]
    new_path = command_list[2]
    if "/" in command:
        dir_path = "/".join(command_list[2].split("/")[:-1])
        os.makedirs(dir_path, exist_ok=True)
    if make_file == "mv":
        shutil.move(old_name, new_path)
