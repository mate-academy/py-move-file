import os


def move_file(command: str) -> None:
    command_sep = command.split()
    if command_sep[0] == "mv":
        old_name = command_sep[1]
        new_name = command_sep[-1].split("/")[-1]
        directory = command_sep[-1].split("/")
        way = ""
        if len(directory) > 1:
            way = "/".join(directory[0: -1: 1]) + "/"
            if not os.path.exists(way):
                os.makedirs(way)
        with open(old_name, "r") as old, open(way + new_name, "w") as new:
            new.write(old.read())
        os.remove(old_name)
