import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    source_file = parts[1]
    destination = parts[2]

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source_file))

    destination_dir = os.path.dirname(destination)

    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    if not os.path.exists(source_file):
        return

    shutil.move(source_file, destination)
