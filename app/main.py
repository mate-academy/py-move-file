import os
import shutil


def move_file(command: str) -> None:
    parts = command.strip().split(" ")

    # Ensure the command is exactly in "mv source destination" format
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. Use: mv source destination")

    source, destination = parts[1], parts[2]

    if not os.path.isfile(source):
        raise FileNotFoundError(f"Source file '{source}' does not exist.")

    destination_dir = os.path.dirname(destination)

    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir, exist_ok=True)

    # Use shutil.move to move/rename the file
    destination_path = os.path.join(destination_dir,
                                    os.path.basename(destination))
    shutil.move(source, destination_path)
