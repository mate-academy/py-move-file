import os


def move_file(command: str) -> None:
    command, first_file, second_file = command.split()
    path = os.path.dirname(second_file)
    if path:
        os.makedirs(path, exist_ok=True)
    os.replace(first_file, second_file)
