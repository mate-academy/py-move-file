import os
import shutil


def move_file(command: str) -> None:
    parts: list[str] = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Wrong command. Format: mv source destination")

    source: str = parts[1]
    destination: str = parts[2]

    if not os.path.isfile(source):
        raise FileNotFoundError(f"File {source} not found.")

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        dir_path: str = os.path.dirname(destination)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

    shutil.move(source, destination)
