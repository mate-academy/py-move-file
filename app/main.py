from os import (
    makedirs,
    path
)

from shutil import move


class MoveCommandSyntaxError(Exception):
    pass


def move_file(command: str) -> None:
    if not command.startswith("mv"):
        raise MoveCommandSyntaxError("Move command not found")

    command = command.split()

    if len(command) != 3:
        raise MoveCommandSyntaxError(
            "Invalid move command syntax.\n"
            "For a successful moving of file "
            "the command should look like this: "
            "mv file.txt some_dir/new_file.txt"
        )

    mv_command, file_to_move, new_file_path = command
    is_consist_directory = "/" in command[-1]

    if is_consist_directory:
        path_of_new_file = path.dirname(new_file_path)

        makedirs(path_of_new_file, exist_ok=True)

    path_of_new_file = new_file_path

    move(file_to_move, path_of_new_file)
