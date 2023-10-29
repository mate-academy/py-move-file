import os


def move_file(command: str) -> None:
    mv, filename, path_to_file = command.split()

    if mv == "mv":
        path = os.path.dirname(path_to_file)
        if path:
            os.makedirs(path, exist_ok=True)

        os.replace(filename, path_to_file)
