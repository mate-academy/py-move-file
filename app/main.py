import os


def move_file(command: str) -> None:
    command, source_file, new_file = command.split()
    if command == "mv":
        path, filename = os.path.split(new_file)
        if path:
            os.makedirs(path, exist_ok=True)
        os.replace(source_file, new_file)
