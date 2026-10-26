import os
import shutil


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "mv":
        raise ValueError("Command must have the format: mv SOURCE DESTINATION")

    _, source_file_path, destination_path = command_parts
    if destination_path.endswith(("/", os.sep)) or (
        os.altsep is not None and destination_path.endswith(os.altsep)
    ):
        destination_path = os.path.join(
            destination_path, os.path.basename(source_file_path)
        )

    destination_directory = os.path.dirname(destination_path)
    if destination_directory:
        os.makedirs(destination_directory, exist_ok=True)

    shutil.move(source_file_path, destination_path)
