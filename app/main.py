from os import makedirs, path
from shutil import move


def move_file(command: str) -> None:
    args = command.split()
    source = args[1]
    destination = args[2].split("/")
    new_filename = destination[-1]
    dirs = []
    if len(destination) > 1:
        dirs = destination[:-1]
        if not path.exists("/".join(dirs)):
            makedirs("/".join(dirs))
    dirs.append(new_filename)
    move(source, "/".join(dirs))
