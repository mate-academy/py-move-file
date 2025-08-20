import os
import shutil


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "mv":
        raise ValueError(
            "Invalid command format. Expected: 'mv source_path "
            "destination_path'"
        )

    mv_command, source_path, destination_path = command_parts

    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file '{source_path}' does not exist")

    if not os.path.isfile(source_path):
        raise ValueError(f"Source '{source_path}' is not a file")

    if destination_path.endswith("/"):
        source_filename = os.path.basename(source_path)
        destination_path = os.path.join(destination_path, source_filename)

    destination_directory = os.path.dirname(destination_path)

    if destination_directory and not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    shutil.move(source_path, destination_path)
