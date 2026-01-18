import os


def move_file(command: str):
    command_split = command.split()
    original_file = command_split[1]
    copy_way = command_split[2]
    copy_way_split = copy_way.split("/")
    copy_file = copy_way_split[-1]
    with open(original_file, "r") as from_file:
        text = from_file.read()
        os.remove(original_file)
        for directory in copy_way_split[0:len(copy_way_split) - 2]:
            os.mkdir(directory)
        with open(copy_file, "w") as to_file:
            to_file.write(text)
