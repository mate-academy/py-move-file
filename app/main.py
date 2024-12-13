import os


def move_file(command: str) -> None:
    command_name, source_file, destination, *_ = command.split()
    if source_file and destination and command_name == "mv":
        end_path, end_file = os.path.split(destination)
        if end_path != "":
            os.makedirs(end_path, exist_ok=True)
        os.replace(source_file, destination)
