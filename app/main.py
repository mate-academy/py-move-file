import os


def move_file(command: str) -> None:
    command, source_file, new_file, *_ = command.split()
    if command == "mv" and source_file != new_file:
        path, filename = os.path.split(new_file)
        if path:
            os.makedirs(path, exist_ok=True)
        os.replace(source_file, new_file)
        if os.path.exists(source_file):
            os.remove(source_file)
