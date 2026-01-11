import os
from os.path import dirname, join


def move_file(command: str) -> None:
    split_command = command.split(" ")

    if split_command[0] != "mv" or len(split_command) != 3:
        return

    source_file = split_command[1]
    destination = split_command[2]

    if destination.endswith("/"):
        destination = join(destination, os.path.basename(source_file))

    if "/" not in command:
        with (open(source_file, "r") as file_in,
                open(destination, "w") as file_out):
            file_out.write(file_in.read())
            os.remove(source_file)

    else:
        directory = dirname(destination)
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        with (open(source_file, "r") as file_in,
              open(destination, "w") as file_out):
            file_out.write(file_in.read())
        os.remove(source_file)
