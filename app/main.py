import shutil
import os


def move_file(command: str) -> None:

    command_list = command.split()

    old_file = command_list[1]
    new_file = "".join(command_list[2].split("/")[-1:])
    dest_new_file = "/".join(command_list[2].split("/")[:-1])
    with open(old_file, "w") as create_file:
        create_file.write("Created new file")
    if not ("mv" in command_list[0]):
        raise ValueError("Input command is not correct.")

    if os.path.exists(old_file) and \
            not ("/" in command_list[2]):
        os.rename(old_file, new_file)

    if os.path.exists(dest_new_file):
        raise Exception("Incorrect path")
    os.makedirs(dest_new_file)
    os.replace(old_file, dest_new_file+"/"+new_file)
