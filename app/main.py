import os


def move_file(command: str) -> None:
    command = command.split()
    path = os.path.dirname(command[2])
    if path:
        if not os.path.exists(path):
            os.makedirs(path)
    os.rename(command[1], command[2])
