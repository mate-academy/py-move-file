import shutil
import os


def move_file(command: str) -> None:

    command_list = command.split()

    old_file = command_list[1]
    new_file = command_list[2]
    dest_new_file = "/".join(new_file.split("/")[:-1])

    if not ("mv" in command_list[0]):
        raise ValueError("Input command is not correct.")

    if os.path.exists(old_file) and \
            not ("/" in new_file):
        os.rename(old_file, new_file)

    os.mkdir(dest_new_file)
    shutil.copy(old_file, new_file)
    os.remove(old_file)
