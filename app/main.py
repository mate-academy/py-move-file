from os import mkdir, rename, chdir, remove
from os.path import exists, dirname


def move_file(command: str) -> None:
    un_command = command.split()

    if len(un_command) != 3 and un_command[0] != "mv":
        raise ValueError("The command is incorrect!")

    file = un_command[1]
    way = un_command[0]

    destination_dir = dirname(way)

    if exists(destination_dir):
        raise ValueError("The file exists!")

    if "/" not in destination_dir:
        rename(file, destination_dir)
    else:
        with open(file, "r") as old_file:
            content = old_file.read()
        remove(file)
        files_list = destination_dir.split("/")
        for file in files_list:
            if file != files_list[-1] and not exists(file):
                mkdir(file)
                chdir(file)
            if file != files_list[-1] and exists(file):
                chdir(file)
        with open(files_list[-1], "w") as new_file:
            new_file.write(content)




