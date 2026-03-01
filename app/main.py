import os


def move_file(command: str) -> None:
    name = command.split()
    if not command or len(name) != 3:
        return
    elif not os.path.exists(name[1]):
        return
    elif name[0] != "mv":
        return
    elif name[1] == name[2]:
        return
    path_to_the_file = name[2].split("/")
    if len(path_to_the_file) == 1:
        os.rename(name[1], name[2])
        return
    os.makedirs(os.path.dirname(name[2]), exist_ok=True)
    os.rename(name[1], name[2])
