import os

from contextlib import contextmanager
from pathlib import Path


@contextmanager
def move_file(command: str) -> None:
    try:
        command, source, target = command.split(maxsplit=3)
    except ValueError:
        raise ValueError("Command must have 'mv' keyword and 2 arguments")

    if command != "mv":
        return

    if "/" in target:
        target_directory = Path(target[:target.rfind("/")])

        if not os.path.exists(target_directory):
            target_directory.mkdir(parents=True, exist_ok=True)

    source_file = open(source, "r")
    target_file = open(target, "w")

    try:
        target_file.write(source_file.read())
    finally:
        source_file.close()
        target_file.close()
        os.remove(source)
