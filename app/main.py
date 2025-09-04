import os
import shutil


def move_file(command: str) -> None:
    parts = command.strip().split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Invalid command format. Expected: mv source destination"
        )

    command_name, source_path, destination_path = parts

    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file '{source_path}' does not exist")

    if not os.path.isfile(source_path):
        raise ValueError(f"Source '{source_path}' must be a file")

    if destination_path.endswith(os.path.sep):
        filename = os.path.basename(source_path)
        destination_path = os.path.join(destination_path, filename)

    dest_dir = os.path.dirname(destination_path)
    if dest_dir:
        create_directories_recursively(dest_dir)

    shutil.copy2(source_path, destination_path)
    os.remove(source_path)


def create_directories_recursively(path: str) -> None:
    if os.path.exists(path):
        return

    parent = os.path.dirname(path)
    if parent and parent != path:
        create_directories_recursively(parent)

    os.mkdir(path)
