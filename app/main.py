import os


def move_file(command: str) -> None:
    parts = command.split(" ")

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command")

    source_path = parts[1]
    destination_path = parts[2]

    if os.path.abspath(source_path) == os.path.abspath(destination_path):
        raise ValueError("Source and destination paths are the same.")

    destination_dir = os.path.dirname(destination_path)
    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    os.rename(source_path, destination_path)
