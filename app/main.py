import os


def move_file(command):
    split_file = command.split(" ")
    if "/" in split_file[-1]:
        path = split_file[-1].split("/")
        os.makedirs("/".join(path[:-1]))
    with open(split_file[1], "r") as file_out,\
            open(split_file[2], "w") as file_in:
        text = file_out.read()
        file_in.write(text)

    os.remove(split_file[1])
