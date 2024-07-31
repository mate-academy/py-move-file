import os
from pathlib import Path


def move_file(command: str) -> None:
    command, source, destination = command.split()
    last_slash = destination.rfind("/")

    Path(destination[:last_slash]).mkdir(parents=True, exist_ok=True)

    with open(source) as src, open(destination, "w") as dst:
        content = src.read()
        dst.write(content)
    os.remove(source)
