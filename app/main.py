import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. Use: mv source destination")

    source = parts[1]
    destination = parts[2]

    if not os.path.isfile(source):
        raise FileNotFoundError(f"Source file '{source}' does not exist")

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        dest_dir = os.path.dirname(destination)
        if dest_dir:
            os.makedirs(dest_dir, exist_ok=True)

    shutil.move(source, destination)
