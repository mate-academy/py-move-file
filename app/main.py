import os


def move_file(command: str) -> None:
    _, old_name, new_name = command.split()
    try:
        os.renames(old_name, new_name)
    except OSError as err:
        print("An error occurred:", err)
