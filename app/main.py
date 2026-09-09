import os
import shutil


def move_file(command: str) -> None:
    if not command:
        return

    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise Exception("Move file not supported")

    _, source, destination = parts

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    destination_dir = os.path.dirname(destination)
    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    shutil.copy(source, destination)
    os.remove(source)
