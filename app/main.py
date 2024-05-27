import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. Use: mv source_file destination_path")

    source = parts[1]
    destination = parts[2]

    if not os.path.isfile(source):
        raise FileNotFoundError(f"No such file: '{source}'")

    if destination.endswith("/"):
        raise ValueError(
            "Destination should not end with a slash unless it is a directory"
        )

    dest_dir = os.path.dirname(destination)

    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    shutil.move(source, destination)
