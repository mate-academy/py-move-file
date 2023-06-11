from os import (
    makedirs,
    path
)

from shutil import move


class MoveCommandSyntaxError(Exception):
    pass


def move_file(command: str) -> None:
    command = command.split()

    if command[0] != "mv":
        raise MoveCommandSyntaxError("Move command not found")

    if len(command) != 3:
        raise MoveCommandSyntaxError(
            "Invalid move command syntax.\n"
            "For a successful moving of file "
            "the command should look like this: "
            "mv file.txt some_dir/new_file.txt"
        )

    file_to_move = command[1]

    try:
        with open(file_to_move) as source:
            source.read()
    except PermissionError:
        raise PermissionError(f"No permission to read the file {source}")

    if not path.exists(file_to_move):
        raise FileNotFoundError(f"File {file_to_move} does not exist")

    is_consist_directory = "/" in command[-1]

    if is_consist_directory:
        path_of_new_file = path.dirname(command[-1])

        if not path.exists(path_of_new_file):
            makedirs(path_of_new_file)

    path_of_new_file = command[-1]

    move(file_to_move, path_of_new_file)
