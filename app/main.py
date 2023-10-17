import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3:
        mv, file_name, destination = command_list
        dirs, file_name_out = os.path.split(destination)
        if mv == "mv":
            if dirs:
                os.makedirs(dirs, exist_ok=True)
            os.rename(file_name, destination)
