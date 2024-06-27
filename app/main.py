import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()

    if parts[0] != "mv" or len(parts) != 3:
        raise ValueError("Invalid command. Use: mv <source> <destination>")

    source, destinat = parts[1], parts[2]

    if not os.path.isfile(source):
        raise FileNotFoundError(f"No such file: '{source}'")

    destination_dir = (
        destinat if destinat.endswith("/") else os.path.dirname(destinat)
    )
    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    shutil.move(source, destinat)
