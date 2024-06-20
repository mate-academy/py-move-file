import os


def move_file(command: str) -> None:
    elements = command.split()
    if elements[0] != "mv":
        raise ValueError

    if "/" not in elements[2]:
        os.rename(elements[1], elements[2])
    else:
        dir_elements = elements[2].split("/")
        path_creator = []
        for dirs in dir_elements[:-1]:
            path_creator.append(dirs)
            path = os.path.join(*path_creator)
            if not os.path.exists(path):
                os.mkdir(path)
        if dir_elements[-1] == "":
            dir_elements.append(elements[1])
        os.rename(elements[1], os.path.join(*dir_elements))
