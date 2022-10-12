from os import mkdir, remove, chdir, listdir, curdir


def directory_exist(directory: str) -> bool:
    for x in listdir(curdir):
        if x == directory:
            return True

    return False


def move_file(command_line: str) -> None:
    _, source, destination = command_line.split(" ")

    if source == destination:
        return

    with open(source, "r") as file:
        data = file.read()
    remove(source)

    path = destination.split("/")

    for directory in path[:-1]:
        if directory_exist(directory):
            chdir(directory)
        else:
            mkdir(directory)
            chdir(directory)

    with open(path[-1], "w") as file:
        file.write(data)
