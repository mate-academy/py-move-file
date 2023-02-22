import os


def move_file(command: str) -> None:
    command, file, directory = command.split()
    if command == "mv":
        os.renames(file, directory)
