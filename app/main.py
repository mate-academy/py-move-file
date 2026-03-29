import os


def move_file(command):
    split = command.split(" ")
    if split[0] == "mv":
        split_direct = split[2].split("/")
        road = ''
        if len(split_direct) > 1:
            for i in range(len(split_direct) - 1):
                road += split_direct[i] + '/'
                os.mkdir(road)
        with open(split[1], "r") as old, open(split[2], "w") as new_place:
            new_place.write(old.read())
            os.remove(split[1])
