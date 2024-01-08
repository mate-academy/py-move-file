import os
import shutil


def move_file(command: str) -> None:
    _, source, destination = command.split()
    if destination.endswith('/'):
        # Ensure the directory exists
        os.makedirs(destination, exist_ok=True)
        # Set the destination file path
        destination = os.path.join(destination, os.path.basename(source))
    else:
        # Check if the destination's parent directory exists, and if not, create it
        parent_dir = os.path.dirname(destination)
        if parent_dir and not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
    shutil.move(source, destination)
