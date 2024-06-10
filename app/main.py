import os


def move_file(command: str) -> None:
    cmd, file_name, direction = command.split()
    dir_ = direction
    if dir_:
        os.makedirs(dir_, exist_ok=True)
    os.replace(file_name, direction)
