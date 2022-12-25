import os


def move_file(command: str) -> None:
    command_list = command.split()
    os.mkdir(command_list[2])
    directory_list = command_list[2].split("/")
    with open(command_list[1], "r") as file, \
            open(directory_list[-1], "w") as new_file:
        new_file.write(file.read())
    os.remove(command_list[1])
