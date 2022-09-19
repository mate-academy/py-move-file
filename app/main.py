import os


def move_file(command):
    split_file = command.split(" ")
    if "/" in split_file[-1]:
        path = split_file[-1].split("/")
        for i in range(len(path) - 1):
            os.mkdir("/".join(path[:i]))
    with open(split_file[1], "r") as file_out,\
            open(split_file[2], "w") as file_in:
        text = file_out.read()
        file_in.write(text)

    os.remove(split_file[1])
