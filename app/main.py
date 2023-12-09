import os
from os import path


def move_file(command: str) -> None:
    if len(command.split()) == 3 and command.split()[0] == "mv":
        _, old_file, new_file = command.split()

        dir_path, new_file = path.split(new_file)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
            new_file_path = os.path.join(dir_path, new_file)
        else:
            new_file_path = new_file

        with (
            open(old_file, "r") as in_file,
            open(new_file_path, "w") as out_file
        ):
            out_file.write(in_file.read())

        os.remove(old_file)
