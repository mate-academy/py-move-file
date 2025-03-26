import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    source_path, destination_path = parts[1], parts[2]

    if not os.path.isfile(source_path):
        raise FileNotFoundError(f"Not such file as {source_path}")

    if destination_path.endswith("/") or os.path.isdir(destination_path):
        os.makedirs(destination_path, exist_ok=True)
        destination_path = os.path.join(destination_path, os.path.basename(source_path))

    shutil.move(source_path, destination_path)
