import os
import shutil


def move_file(command: str) -> None:
    command_parts = command.strip().split()

    if len(command_parts) != 3 or command_parts[0] != "mv":
        raise ValueError(
            "Invalid command format. Use: mv <source> <destination>"
        )

    source_file_path = command_parts[1]
    destination_file_path = command_parts[2]

    if not source_file_path or not destination_file_path:
        raise ValueError("Source and destination paths cannot be empty.")

    if source_file_path == destination_file_path:
        raise ValueError("Source and destination paths must be different.")

    if not os.path.isfile(source_file_path):
        raise FileNotFoundError(
            f"Source file '{source_file_path}' does not exist."
        )

    if destination_file_path.endswith("/"):
        destination_file_path = os.path.join(
            destination_file_path, os.path.basename(source_file_path)
        )

    destination_dir = os.path.dirname(destination_file_path)

    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    shutil.move(source_file_path, destination_file_path)
