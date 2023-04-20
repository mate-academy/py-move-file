import os
import shutil


def move_file(command):
    cmd_parts = command.split()

    if len(cmd_parts) != 3 or cmd_parts[0] != "mv":
        raise ValueError("Invalid command format. Use: mv source destination")

    _, source, destination = cmd_parts

    head, tail = os.path.split(destination)

    if not tail:
        destination = os.path.join(head, os.path.basename(source))

    destination_dir = os.path.dirname(destination)

    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    shutil.move(source, destination)
