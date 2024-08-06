import os


def move_file(command: str) -> None:

    user_command, source_file, result_file = command.split()

    os.renames(source_file, result_file)
