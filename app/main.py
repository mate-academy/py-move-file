import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, destination = parts

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    destination_directory = os.path.dirname(destination)
    if destination_directory and not os.path.isdir(destination_directory):
        os.makedirs(destination_directory)

    try:
        shutil.copy(source, destination)
        os.remove(source)
    except FileNotFoundError:
        return
