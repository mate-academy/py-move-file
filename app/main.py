import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3:
        command_name, file_name, destination = command_list
        dirs, _ = os.path.split(destination)
        if command_name == "mv":
            if dirs:
                os.makedirs(dirs, exist_ok=True)
            os.replace(file_name, destination)
