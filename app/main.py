import os
from os.path import dirname


def move_file(command: str) -> None:
    split_command = command.split(" ")
    source_file = split_command[1]
    destination = split_command[2]

    if split_command[0] == "mv" and len(split_command) == 3:
        if "/" not in command:
            with (open(source_file, "r") as file_in,
                  open(destination, "w") as file_out):
                file_out.write(file_in.read())
                os.remove(source_file)

        else:
            try:
                directory = dirname(destination)
                if not os.path.exists(directory):
                    os.makedirs(directory)
            except FileExistsError:
                pass

            with (open(source_file, "r") as file_in,
                  open(destination, "w") as file_out):
                file_out.write(file_in.read())
                os.remove(source_file)
