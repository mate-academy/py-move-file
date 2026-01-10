import os

from typing import Any, TextIO


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = open(filename, "r")

    def __enter__(self) -> TextIO:
        return self.file

    def __exit__(self, element_type: Any, value: Any, traceback: Any) -> None:
        self.file.close()
        if os.path.exists(self.filename):
            os.remove(self.filename)


def move_file(command: str) -> None:
    commands = command.split(" ")
    if len(commands) != 3:
        return
    elif commands[0] != "mv":
        return
    elif commands[1] == "":
        return
    elif commands[2] == "":
        return

    try:
        os.makedirs(os.path.split(commands[2])[0], exist_ok=True)
    except FileNotFoundError:
        pass

    with CleanUpFile(commands[1]) as source_file:
        with open(commands[2], "w") as target_file:
            target_file.write(source_file.read())
