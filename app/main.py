import os


def move_file(command: str) -> None:
    command_name, file_name, file_path, *_ = command.split()

    if command_name != "mv":
        return

    directory = os.path.dirname(file_path)
    if directory:
        os.makedirs(directory, exist_ok=True)

    os.rename(file_name, file_path)
