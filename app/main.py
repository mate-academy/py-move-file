import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format")
    source_file = parts[1]
    destination_path = parts[2]
    if not os.path.isfile(source_file):
        raise FileNotFoundError(f"Source file '{source_file}' does not exist")
    if destination_path.endswith("/"):
        raise (ValueError
               ("Destination path cannot end with a '/' "
                "as it should be a file path"))
    destination_dir = os.path.dirname(destination_path)
    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)
    shutil.move(source_file, destination_path)
