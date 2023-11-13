import os


def move_file(command: str) -> None:
    curr_file, full_path = command.split(" ")[1:]
    path, new_file = os.path.split(full_path)

    if path:
        os.makedirs(path, exist_ok=True)

    os.replace(curr_file, full_path)
