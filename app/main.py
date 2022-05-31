import os


def move_file(command: str):
    old = command.split()[1]
    new = command.split()[2]

    if '/' not in new:
        os.rename(old, new.split("/")[-1])
        return

    new_dir = "/".join(new.split("/")[:-1])
    os.makedirs(new_dir)
    os.rename(old, new)


move_file('mv file.txt files/siska/file2.txt')