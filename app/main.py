import os


def move_file(command: str):
    commands = command.split()
    file_to_copy = commands[1]
    file_to_create = commands[2]

    with open(file_to_copy, "r") as file:
        data = file.read()

    root = ""
    dirs = file_to_create.split("/")[:-1]

    for directory in dirs:
        root += directory + "/"
        os.mkdir(root)

    with open(file_to_create, "w") as file:
        file.write(data)

    os.remove(file_to_copy)
