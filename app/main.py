import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    source = parts[1]
    destination, filename = os.path.split(parts[2])

    if parts[0] == "mv" and len(parts) == 3:
        if destination:
            os.makedirs(destination, exist_ok=True)
        shutil.copy(source, os.path.join(destination, filename))

    os.remove(source)
