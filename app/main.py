import os
import shutil


def move_file(command: str) -> None:

    command, command_old_file, command_new_file = command.split()
    if (command_old_file.split(".")[1] != command_new_file.split(".")[1]
            or command != "mv"):
        raise ValueError("Error in entered data!")

    directory, new_file = os.path.split(command_new_file)

    if not directory:
        os.rename(command_old_file, new_file)
        return

    os.makedirs(directory, exist_ok=True)
    shutil.copy(command_old_file, command_new_file)
    os.remove(command_old_file)
