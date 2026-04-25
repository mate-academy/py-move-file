import os
from shutil import copyfile


def move_file(move_command: str) -> None:

    # Split the command into parts
    parts = move_command.split()

    # Check if the command is in the correct format
    if len(parts) != 3 or parts[0] != "mv":
        print("Invalid command format. Use: mv <source> <destination>")
        return

    _, source_file, dest_file = parts

    is_dest_directory = dest_file[-1] == "/"

    # Check if the source file exists
    if not os.path.isfile(source_file):
        print(f"Source file '{source_file}' does not exist.")
        return

    # Check directory structure of the destination
    dest_dir = os.path.dirname(dest_file)

    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

        # If the destination is a directory,
        # move the file into that directory
        if is_dest_directory:
            dest_file = os.path.join(dest_dir, os.path.basename(source_file))

    # Move the file
    copyfile(source_file, dest_file)
    os.remove(source_file)
