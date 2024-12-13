from os import mkdir, rename, chdir, remove
from os.path import exists, dirname


def move_file(command: str) -> None:
    un_command = command.split()

    if len(un_command) != 3 and un_command[0] != "mv":
        raise ValueError("The command is incorrect!")

    old_file = un_command[1]
    way = un_command[0]
    destination_dir = dirname(way)

    if exists(destination_dir):
        raise ValueError("The file exists!")

    if "/" not in destination_dir:
        rename(old_file, destination_dir)
    else:
        with open(old_file, "r") as current_file:
            content = current_file.read()
        remove(old_file)
        files_list = destination_dir.split("/")
        for name_file in files_list:
            if name_file != files_list[-1] and not exists(name_file):
                mkdir(name_file)
                chdir(name_file)
            if name_file != files_list[-1] and exists(name_file):
                chdir(name_file)
        with open(files_list[-1], "w") as new_file:
            new_file.write(content)
