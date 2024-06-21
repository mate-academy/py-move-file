import os


def move_file(command: str) -> None:
    elements = command.split()
    if len(elements) != 3 and elements[0] != "mv":
        raise Exception("Incorrect command")

    source, destination = elements[1:]
    head, tail = os.path.split(destination)
    if not head:
        os.rename(source, destination)
    else:
        folders = head.split("/")
        path_creator = []
        for folder in folders:
            path_creator.append(folder)
            path = os.path.join(*path_creator)
            if not os.path.exists(path):
                os.mkdir(path)
        if not tail:
            os.rename(source, os.path.join(head, source))
        else:
            os.rename(source, destination)
