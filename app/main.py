import os


def move_file(command: str) -> None:
    command, file_in, file_out_with_rout = command.split()
    if command == "mv":
        os.renames(file_in, file_out_with_rout)
