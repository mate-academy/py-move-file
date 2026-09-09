import os

from pathlib import Path


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[0] == "mv" and Path(parts[1]).is_file():
        source = Path(parts[1])
        destination = Path(parts[2])
        if parts[2].endswith("/"):
            destination.mkdir(parents=True, exist_ok=True)
            destination /= source.name
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)

        with open(source, "r") as file1, open(destination, "w") as file2:
            file2.write(file1.read())
            os.remove(source)
