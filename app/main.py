import os


def move_file(command: str) -> None:
    command, source_path, destination_path = command.split()
    directory, filename = os.path.split(destination_path)
    if not directory:
        os.rename(source_path, destination_path)
        return
    os.makedirs(directory, exist_ok=True)
    os.rename(source_path, destination_path)
