import os
import shutil


def move_file(command: str) -> None:
    # Split the command into parts, skipping "mv" if present
    parts = command.split()
    if parts[0] == "mv":
        parts = parts[1:]

    if len(parts) != 2:
        raise ValueError("Invalid command format. "
                         + "Expected: mv source destination")

    source, destination = parts

    # Check if source file exists
    if not os.path.exists(source):
        raise FileNotFoundError(f"Source file '{source}' does not exist")

    # Check if source is a file (not a directory)
    if not os.path.isfile(source):
        raise ValueError(f"'{source}' is not a file")

    # If destination ends with '/', append the source filename
    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    # Create all necessary directories in the destination path
    dest_dir = os.path.dirname(destination)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    # Move the file
    shutil.move(source, destination)
