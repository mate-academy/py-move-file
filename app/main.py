import os
from pathlib import Path


def move_file(command: str) -> None:
    try:
        command, current_destination, target_destination = command.split(" ")

        if command != "mv":
            print(f"Command {command} is not supported!")
            return

        if current_destination == target_destination:
            print("There is nothing to move, paths are same!")
            return

        if not os.path.isfile(current_destination):
            print("Target file does not exist!")
            return

        target_destination = target_destination.replace("\\", "/")

        if "/" in target_destination:
            target_dirs = "/".join(target_destination.split("/")[:-1])
            os.makedirs(target_dirs, exist_ok=True)

        Path(current_destination).rename(target_destination)
    except ValueError:
        print("Failed to parse command!")
