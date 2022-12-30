import os


def move_file(command: str) -> None:
    mv, old_file_path, new_file_path = command.split()
    if mv == "mv" and not os.path.exists(new_file_path):
        os.renames(old_file_path, new_file_path)
