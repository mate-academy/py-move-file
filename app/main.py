import os


def move_file(command: str) -> None:
    if command.startswith("mv"):
        mv, file, path = command.split()
        if "/" not in command:
            os.rename(file, path)
        else:
            os.makedirs(path[:path.rfind("/")])
            os.replace(file, path)
