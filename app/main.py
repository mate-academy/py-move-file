import os.path
import shutil


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        raise ValueError("Invalid number of arguments in the command")

    source = parts[1]
    destination = parts[2]

    if not os.path.exists(source):
        raise FileNotFoundError(f"Source file '{source}' does not exist")
    if not os.path.isfile(source):
        raise ValueError(f"'{source}' is not a file")

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    destination_dir = os.path.dirname(destination)

    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir, exist_ok=True)

    shutil.move(source, destination)

    print(f"File moved from {source} to {destination}")
