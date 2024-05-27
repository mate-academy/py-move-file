import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. Use: mv source destination")

    source_path, destination_path = parts[1:]

    if not os.path.isfile(source_path):
        raise FileNotFoundError(f"No such file: '{source_path}'")

    if destination_path.endswith("/"):
        destination_dir = dest
        destination_file = os.path.join(destination_dir, os.path.basename(source_path))
    else:
        destination_dir = os.path.dirname(destination_path)
        dest_file = dest

    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    shutil.move(source_path, destination_path)
