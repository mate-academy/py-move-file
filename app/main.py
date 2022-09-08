from os import mkdir, remove


def move_file(command: str):
    list_command = command.split()
    if "/" in list_command[-1]:
        path_list = list_command[-1].split("/")
        for i in range(len(path_list) - 1):
            mkdir("/".join(path_list[:i]))
    with open(list_command[1], "r") as r, open(list_command[2], "w") as w:
        w.write(r.read())
    remove(list_command[1])
