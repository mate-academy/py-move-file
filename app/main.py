import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. "
                         "Expected 'mv <source> <destination>'.")
    _, source, destination = parts
    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))
    dir_name = os.path.dirname(destination)
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name)
    shutil.move(source, destination)
