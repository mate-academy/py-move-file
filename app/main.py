from os import makedirs, remove
from pathlib import Path


def move_file(command: str) -> None:
    command_ls = command.split()

    if len(command_ls) == 3 and command_ls[0] == "mv":
        source_filename, destination = command_ls[1], command_ls[2]
        makedirs(Path(destination).parent, exist_ok=True)

        with (
            open(source_filename, "r") as source_file,
            open(destination, "w") as destination_file
        ):
            destination_file.write(source_file.read())

        remove(source_filename)
