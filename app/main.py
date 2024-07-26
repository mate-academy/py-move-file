import os


def move_file(command: str) -> None:
    command, file_name, move_to = command.split()
    directories = []

    if "/" in move_to:
        move_to = move_to.split("/")
        directories = move_to[:-1]
        move_to = move_to[-1]

    path = ""
    for item in directories:
        path += item
        if not os.path.exists(path):
            os.mkdir(path)
        path += "/"

    try:
        with open(file_name, "r") as file, open(path + move_to, "w") as moving:

            moving.writelines(file.readlines())

    except OSError as e:
        print(e)
    else:
        os.remove(file_name)
