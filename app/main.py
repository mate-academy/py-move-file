import os


def move_file(command: str) -> None:
    command_list = command.split(" ")
    directory_list = command_list[2].split("/")
    if len(directory_list) != 1:
        if ".txt" in directory_list[-1]:
            os.mkdir("/".join(directory_list[:-1]))
        else:
            os.mkdir(command_list[2])
            command_list[2] += command_list[1]
    with open(command_list[1], "r") as file, \
            open(command_list[2], "w") as new_file:
        new_file.write(file.read())
    os.remove(command_list[1])
