import os
import shutil


def move_file(command):
    cmd_parts = command.split()

    if len(cmd_parts) != 3 or cmd_parts[0] != "mv":
        raise ValueError("Invalid command format. Use: mv source destination")

    source, destination = cmd_parts[1], cmd_parts[2]

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    destination_dir = os.path.dirname(destination)
    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    shutil.move(source, destination)
