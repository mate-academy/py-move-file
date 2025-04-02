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

    if destination_dir and not os.path.exists(destination_dir):
        try:
            os.makedirs(destination_dir)
        except FileExistsError:
            pass

    shutil.move(source_file, destination)
