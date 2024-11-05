import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command. "
                         "Please use the format 'mv source destination'.")

    _, source, destination = parts

    if not os.path.isfile(source):
        raise FileNotFoundError(f"The source file '{source}' does not exist.")

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        destination_dir = os.path.dirname(destination)

        if destination_dir and not os.path.exists(destination_dir):
            os.makedirs(destination_dir, exist_ok=True)

    shutil.move(source, destination)
