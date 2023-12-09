import os
from os import path


def move_file(command: str) -> None:
    commands = command.split()
    if len(commands) == 3 and commands[0] == "mv":
        _, old_file, new_file = commands

        dir_path, name = path.split(new_file)
        if dir_path:
            os.makedirs(dir_path)

        with (
            open(old_file, "r") as in_file,
            open(new_file, "w") as out_file
        ):
            out_file.write(in_file.read())
        os.remove(old_file)
