import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3:
        mv_command, source_file, destination_path = command.split()
        if mv_command == "mv":
            path_file = os.path.dirname(destination_path)
            if path_file:
                os.makedirs(path_file, exist_ok=True)
            os.replace(source_file, destination_path)
