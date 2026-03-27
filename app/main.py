import os


def move_file(command: str) -> None:
    mv, old_file, new_file = command.split(" ")
    if old_file == new_file:
        return
    new_dir = os.path.dirname(new_file)
    if new_dir:
        os.makedirs(new_dir, exist_ok=True)
    os.replace(old_file, new_file)
