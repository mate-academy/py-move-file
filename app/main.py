import os
import shutil


def move_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. Use: mv source destination")

    source, destination = parts[1], parts[2]

    if not os.path.isfile(source):
        raise FileNotFoundError(f"Source file '{source}' does not exist.")

    # Extract directory name if present
    destination_dir = os.path.dirname(destination)

    # Create directories only if destination has a directory part
    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    shutil.move(source, destination)
