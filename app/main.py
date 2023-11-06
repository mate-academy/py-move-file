import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        mv, file, directory = command.split()
        if mv == "mv":
            path = os.path.dirname(directory)
            if path:
                os.makedirs(path, exist_ok=True)
            os.replace(file, directory)
