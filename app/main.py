from os import makedirs, path
from shutil import move


def move_file(command: str) -> None:
    _, source, destination = command.split()
    destination = destination.split("/")
    new_filename = destination[-1]
    dirs = []
    if len(destination) > 1:
        dirs = destination[:-1]
        makedirs(path.join(*dirs), exist_ok=True)
    dirs.append(new_filename)
    move(source, "/".join(dirs))
