import os
import shutil


def move_file(command: str) -> None:
    cmd_parts = command.split()

    if len(cmd_parts) != 3 or cmd_parts[0] != "mv":
        raise ValueError("Invalid command format. Use: mv source destination")

    _, source, destination = cmd_parts

    head, tail = os.path.split(destination)

    if head:
        os.makedirs(head, exist_ok=True)

    shutil.move(source, destination)
