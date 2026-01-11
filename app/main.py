import os


def move_file(command: str) -> None:
    mv, source_file, destination_path = command.split()
    if mv == "mv":
        path = os.path.dirname(destination_path)
        if path:
            os.makedirs(path, exist_ok=True)
        os.replace(source_file, destination_path)
