import os
import shutil


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3:
        command_name, source, destination = command_list
    else:
        return
    if "/" in command:
        dir_path = os.path.dirname(destination)
        os.makedirs(dir_path, exist_ok=True)
    if command_name == "mv":
        shutil.copy(source, destination)
        os.remove(source)
