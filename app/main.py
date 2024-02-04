import os


def move_file(command: str) -> None:
    command, original_file, full_path = command.split()

    if command == "mv":
        directory, file = os.path.split(full_path)

        if directory == "":
            os.rename(original_file, file)
        else:
            directory_path = os.path.dirname(full_path)
            os.makedirs(directory_path, exist_ok=True)
            os.rename(original_file, full_path)
