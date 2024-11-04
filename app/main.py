import os


def move_file(command: str) -> None:

    mv, source_file, destination = command.split()
    if mv != "mv":
        return

    if "/" in destination:
        if destination[-1] == "/":
            destination += source_file

        dir_list = destination.split("/")
        dir_list.pop()
        directory = ""
        for dirs in dir_list:
            directory += dirs
            directory += "/"

        if not os.path.isdir(directory):
            os.makedirs(directory)

    sf = open(source_file, "r")
    source_text = sf.read()
    cf = open(destination, "w")
    cf.write(source_text)
    sf.close()
    cf.close()
    os.remove(source_file)
