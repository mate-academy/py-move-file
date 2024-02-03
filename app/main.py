import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command")

    source, destination = parts[1], parts[2]

    if destination.endswith("/") or os.path.isdir(destination):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        parent_dir = os.path.dirname(destination)
        # Call os.makedirs only if parent_dir is not empty
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)

    shutil.move(source, destination)
    print(f"Moved '{source}' to '{destination}'")
