import os


def move_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) == 3 and split_command[0] == "mv":
        mod, original_file, moved_file = split_command

        directory = os.path.dirname(moved_file)
        if directory:
            os.makedirs(directory, exist_ok=True)
        os.rename(original_file, moved_file)
