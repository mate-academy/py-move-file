import os
import shutil


def move_file(command: str) -> None:
    parts = command.strip().split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Command must be in format: mv source target")

    source = parts[1]
    destination = parts[2]

    if not os.path.isfile(source):
        raise FileNotFoundError(f"Source file '{source}' does not exist")

    if destination.endswith("/"):
        destination = destination.rstrip("/")
        os.makedirs(destination, exist_ok=True)
        dest_path = os.path.join(destination, os.path.basename(source))
    else:
        dest_dir = os.path.dirname(destination)
        if dest_dir:
            os.makedirs(dest_dir, exist_ok=True)
        dest_path = destination

    shutil.copy2(source, dest_path)

    os.remove(source)
