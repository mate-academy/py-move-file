import os
import shutil


def move_file(command: str) -> None:
    command = command.split()
    if len(command) != 3 or command[0] != "mv":
        raise ValueError(f"Invalid command: {command}")

    source_path = command[1]
    destination_path = command[2]

    if not os.path.isfile(source_path):
        raise FileNotFoundError(f"Source file does not exist: {source_path}")
    if not destination_path or destination_path.isspace():
        raise ValueError("Destination path is invalid or empty.")

    if destination_path.endswith("/"):
        os.makedirs(destination_path, exist_ok=True)
        destination_path = os.path.join(
            destination_path, os.path.basename(source_path)
        )
    else:
        dir_path = os.path.dirname(destination_path)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

    shutil.move(source_path, destination_path)
