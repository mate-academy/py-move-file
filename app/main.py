import os
import shutil
from typing import Optional


def move_file(command: str) -> Optional[str]:
    # Split the command into parts
    parts = command.split()

    # Check if the command is 'mv' and has the correct number of arguments
    if parts[0] != "mv" or len(parts) != 3:
        print("Invalid command")
        return

    source = parts[1]
    destination = parts[2]

    # Check if the source file exists
    if not os.path.isfile(source):
        print(f"Source file {source} does not exist")
        return

    # If the destination ends with '/', it's a directory
    if destination.endswith("/"):
        # Create the directory if it doesn't exist
        os.makedirs(destination, exist_ok=True)
        # Move the file
        shutil.move(source, destination)
    else:
        # If the destination includes directories, create them
        destination_dir = os.path.dirname(destination)
        if destination_dir != "":
            os.makedirs(destination_dir, exist_ok=True)
        # Move (or rename) the file
        shutil.move(source, destination)

    print(f"Moved {source} to {destination}")
