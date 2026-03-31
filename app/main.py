import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. Use: mv source destination")

    source_path, destination_path = parts[1], parts[2]

    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file '{source_path}' does not exist.")

    destination_dir = os.path.dirname(destination_path)

    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    shutil.move(source_path, destination_path)
