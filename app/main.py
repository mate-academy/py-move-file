import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        command_name, file_name, mv_file = command.split()
        directories, file_name_out = os.path.split(mv_file)
        if command_name == "mv" and os.path.isfile(file_name):
            if directories:
                os.makedirs(directories, exist_ok=True)
            os.rename(file_name, mv_file)
