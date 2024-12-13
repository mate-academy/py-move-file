import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 and parts[0] != "mv":
        return

    cmd, source, destination = parts

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination_path = os.path.join(destination,
                                        os.path.basename(source))
    else:
        parent_dir = os.path.dirname(destination)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)
        destination_path = destination

    shutil.move(source, destination_path)
