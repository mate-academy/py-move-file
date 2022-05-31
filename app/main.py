import os


def move_file(command: str):
    old = command.split()[1]
    new = command.split()[2]

    new_dir = "/".join(new.split("/")[:-1])
    os.makedirs(new_dir)
    os.rename(old, new)
