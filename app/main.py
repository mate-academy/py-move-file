import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        command, source_file, directory = command.split()
    else:
        return

    if command != "mv" or not source_file or not directory:
        return

    file_dir = os.path.dirname(directory)

    if file_dir:
        os.makedirs(file_dir, exist_ok=True)
    os.replace(source_file, directory)
