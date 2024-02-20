import os


def move_file(command: str) -> None:
    ls_of_command = command.split()
    if len(ls_of_command) == 3:
        command, source_file, path_file = command.split()
        if command == "mv" and os.path.dirname(path_file):
            os.makedirs(os.path.dirname(path_file), exist_ok=True)
        os.rename(source_file, path_file)
