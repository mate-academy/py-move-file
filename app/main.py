import os


def move_file(values: str):
    values = values.split()
    path = values[2].split("/")
    with open(values[1], "r") as file_in:
        content = file_in.read()
    os.remove(values[1])
    if len(path) == 2:
        os.mkdir(path[0])
    if len(path) == 3:
        os.mkdir(path[0])
        os.mkdir(path[0] + "/" + path[1])
    if len(path) == 4:
        os.mkdir(path[0])
        os.mkdir(path[0] + "/" + path[1])
        os.mkdir(path[0] + "/" + path[1] + "/" + path[2])
    with open(values[2], "w") as file_out:
        file_out.write(content)
