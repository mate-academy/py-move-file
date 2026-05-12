import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(f"Invalid command: {command}")

    source = parts[1]
    destination = parts[2]

    if destination.endswith("/"):
        directory = destination
        destination_path = os.path.join(destination, os.path.basename(source))
    else:
        directory = os.path.dirname(destination)
        destination_path = destination

    if directory:
        os.makedirs(directory, exist_ok=True)

    shutil.copy2(source, destination_path)
    os.remove(source)
