from shutil import move
from os import makedirs
from os.path import dirname


def move_file(command: str) -> None:
    params = command.split()
    if len(params) == 3 and params[0] == "mv":
        dest_dir = dirname(params[2])
        if dest_dir != "":
            makedirs(dest_dir, exist_ok=True)
        move(params[1], params[2])
