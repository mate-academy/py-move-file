import os


def move_file(command: str) -> None:
    parts = command.split(" ")
    source_path = parts[1]
    destination_path = parts[2]

    destination_dir = os.path.dirname(destination_path)
    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    os.rename(source_path, destination_path)
