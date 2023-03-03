import os
import shutil


def move_file(command: str) -> None:
    command = command.split(" ")
    if "mv" not in command or len(command) != 3:
        return

    if "/" not in command[2]:
        os.rename(command[1], command[2])
        return

    if os.path.exists(command[2]):
        return

    file_name = command[1]
    new_file_name = os.path.split(command[2])[1]
    path = os.path.split(command[2])[0]

    os.rename(file_name, new_file_name)

    try:
        os.makedirs(path)
    except FileExistsError:
        shutil.move(new_file_name, path)
    else:
        shutil.move(new_file_name, path)
