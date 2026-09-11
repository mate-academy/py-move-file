import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Command must be in format: 'mv <source> <destination>'"
        )

    source = parts[1]
    destination = parts[2]

    if not os.path.exists(source):
        raise FileNotFoundError(
            f"Source file '{source}' does not exist."
        )

    if not os.path.isfile(source):
        raise ValueError("Source must be a file, not a directory")

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    destination_dir = os.path.dirname(destination)

    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    shutil.copy2(source, destination)
    os.remove(source)
