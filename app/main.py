import os
from pathlib import Path


def move_file(command: str) -> None:
    try:
        if len(command.split(" ")) != 3:
            raise ValueError("Failed to parse command!")

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

        if target_destination.endswith("/"):
            target_destination = os.path.join(
                target_destination, os.path.basename(current_destination)
            )

        destination_dir = os.path.dirname(target_destination)

        if destination_dir:
            os.makedirs(destination_dir, exist_ok=True)

        Path(current_destination).rename(target_destination)
    except ValueError as error:
        print(error)
