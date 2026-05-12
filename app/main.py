import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(f"Invalid command: {command}")

    _, source, destination = parts

    if destination.endswith("/"):
        directory = destination
        destination_path = os.path.join(destination, os.path.basename(source))
    else:
        directory = os.path.dirname(destination)
        destination_path = destination

    if directory:
        path = ""
        for part in directory.split("/"):
            if part:
                path = os.path.join(path, part) if path else part
                if not os.path.exists(path):
                    os.mkdir(path)

    shutil.copy2(source, destination_path)
    os.remove(source)
