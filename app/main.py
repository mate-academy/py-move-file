import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Command must be in the format 'mv source destination'")

    source = parts[1].strip()
    destination = parts[2].strip()

    if not source or not destination:
        raise ValueError("'source' and 'destination' cannot be empty")

    if not os.path.exists(source):
        raise FileNotFoundError(f"File {source} does not exist")

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        destination_dir = os.path.dirname(destination)
        if destination_dir and not os.path.exists(destination_dir):
            os.makedirs(destination_dir, exist_ok=True)

    shutil.move(source, destination)
