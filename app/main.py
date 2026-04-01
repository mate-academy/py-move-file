import os


def move_file(command: str) -> None:
    flag, file_name, move_to = command.split()

    if flag == "mv":
        dirs = os.path.dirname(move_to)
        if dirs:
            os.makedirs(dirs, exist_ok=True)
        os.replace(file_name, move_to)
