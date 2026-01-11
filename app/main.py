import os
import shutil


def move_file(command: str) -> None:
    mode, source, destination = command.split()

    if mode != "mv" or source == destination:
        raise ValueError("use: mv source destination")

    if not os.path.exists(source):
        raise FileNotFoundError(f"File {source} not found")

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    destination_directory = os.path.dirname(destination)

    if destination_directory:
        os.makedirs(destination_directory, exist_ok=True)

    shutil.move(source, destination)
