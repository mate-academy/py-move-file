import os


def move_file(command: str) -> None:
    split_command = command.split(" ")
    original_file = split_command[1]
    moved_file = split_command[2]

    directory = os.path.dirname(moved_file)
    if directory:
        os.makedirs(directory, exist_ok=True)
    os.rename(original_file, moved_file)
