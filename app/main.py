import os


def move_file(command: str) -> None:
    command_list = command.split()

    if len(command_list) < 3 or command_list[0] != "mv":
        print("command wrong")
        return

    if "/" not in command_list[2]:
        os.rename(command_list[1], command_list[2])
        return

    patch, name = os.path.split(command_list[2])
    os.rename(command_list[1], name)
    os.makedirs(patch)
    os.replace(name, command_list[2])
