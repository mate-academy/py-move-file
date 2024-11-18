import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command. Use: mv source destination")

    source = parts[1]
    destination = parts[2]

    if not os.path.isfile(source):
        raise FileNotFoundError(f"No such file: '{source}'")

    if destination.endswith("/"):
        dest_dir = destination
        dest_file = os.path.join(dest_dir, os.path.basename(source))
    else:
        dest_file = destination
        dest_dir = os.path.dirname(dest_file)

    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    shutil.move(source, dest_file)
