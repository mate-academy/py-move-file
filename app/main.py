import os


def move_file(command: str) -> None:
    command_list = command.split()
    command_move = command_list[0]
    source_file = command_list[1]
    destination = command_list[2]

    if len(command_list) < 3 or command_move != "mv":
        print("command wrong")
        return

    if "/" not in destination:
        os.rename(source_file, destination)
        return

    patch, name = os.path.split(destination)
    os.rename(source_file, name)
    os.makedirs(patch)
    os.replace(name, destination)
