import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        raise ValueError("Invalid command format. "
                         "Expected 'mv source destination'.")
    source = parts[1]
    destination = parts[2]
    if not os.path.isfile(source):
        raise FileNotFoundError(f"Source file'{source}' not found.")
    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))
    destination_dir = os.path.dirname(destination)
    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    shutil.move(source, destination)
    print(f"File '{source}' successfully moved to '{destination}'.")
