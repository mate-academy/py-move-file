import os


def move_file(command: str) -> None:
    elements = command.split()
    if len(elements) != 3 and elements[0] != "mv":
        raise Exception("Incorrect command")

    source = elements[1]
    destination = elements[2]
    if "/" not in destination:
        os.rename(source, destination)
    else:
        dir_elements = destination.split("/")
        path_creator = []
        for dirs in dir_elements[:-1]:
            path_creator.append(dirs)
            path = os.path.join(*path_creator)
            if not os.path.exists(path):
                os.mkdir(path)
        if dir_elements[-1] == "":
            dir_elements.append(source)
        os.rename(source, os.path.join(*dir_elements))
