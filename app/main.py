import os
import shutil


def move_file(command: str) -> None:
    """

    Args:
        command (str): A command string in the format `mv source destination`.
    """
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise \
            (ValueError
             ("Invalid command format. "
              "Expected format: 'mv source destination'"))

    _, source, destination = parts

    if not os.path.isfile(source):
        raise FileNotFoundError(f"Source file '{source}' does not exist.")

    # Check if destination ends with '/' (indicating a directory)
    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        # Ensure the destination directory exists
        dest_dir = os.path.dirname(destination)
        if dest_dir:
            os.makedirs(dest_dir, exist_ok=True)

    # Move file
    shutil.move(source, destination)

    # Verify that source no longer exists
    if os.path.exists(source):
        raise RuntimeError(f"Failed to remove "
                           f"source file '{source}' after moving.")
