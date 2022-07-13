import os


def move_file(command: str):
    commands = command.split()
    file_first = commands[1]
    file_second = command[2]

    with open(file_first, "r") as f:
        file = f.read()

    path_to_folder = ""
    path = file_second.split("/")[:-1]
    for name in path:
        path_to_folder = f"{name}/"
        os.mkdir(path_to_folder)

    with open(file_second, "w") as file_2:
        file_2.write(file)

    os.remove(file_first)
