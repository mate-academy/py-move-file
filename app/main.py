import os

from pathlib import Path


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

    with open(source, "r") as source_file, open(target, "w") as target_file:
        target_file.write(source_file.read())

    os.remove(source)
