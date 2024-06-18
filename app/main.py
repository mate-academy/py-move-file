import os


def move_file(command: str) -> None:
    cmd, file_name, direction = command.split()

    if direction:
        os.makedirs(direction, exist_ok=True)
    os.replace(file_name, direction)
