import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3:

        command_name, file_name, mv_file = command_list
        dirs, _ = os.path.split(mv_file)

        if command_name == "mv" and os.path.isfile(file_name):
            if dirs:
                os.makedirs(dirs, exist_ok=True)
            os.replace(file_name, mv_file)
