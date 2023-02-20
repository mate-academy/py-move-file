import os


def move_file(command: str) -> None:
    command_sep = command.split()
    if command_sep[0] == "mv":
        old_name = command_sep[1]
        new_name = command_sep[-1].split("/")[-1]
        way = command_sep[-1].split("/")
        directory = ""
        if len(way) > 1:
            directory = "/".join(way[0: -1: 1]) + "/"
            if not os.path.exists(directory):
                os.makedirs(directory)
        with open(old_name, "r") as old:
            with open(directory + new_name, "w") as new:
                new.write(old.read())
        os.remove(old_name)
