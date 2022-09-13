from os import mkdir, remove


def move_file(command: str):
    list_command = command.split()
    if list_command[0] != "mv" and len(list_command) != 3:
        return "Wrong command"
    if "/" in list_command[-1]:
        path_list = list_command[-1].split("/")
        for i in range(len(path_list) - 1):
            mkdir("/".join(path_list[:i]))
    with open(list_command[1], "r") as first_file, open(list_command[2], "w") as second_file:
        second_file.write(first_file.read())
    remove(list_command[1])
