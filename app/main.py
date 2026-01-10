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


class MoveFile:
    def __init__(self, patch: str, source_name: str) -> None:
        self.filename = source_name
        if patch.endswith("/"):
            self.file = open(os.path.join(patch, "/", source_name), "w")
        else:
            self.file = open(os.path.join(patch, source_name), "w")

    def __enter__(self) -> TextIO:
        return self.file

    def __exit__(self, element_type: Any, value: Any, traceback: Any) -> None:
        self.file.close()


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

    patch, file_move = os.path.split(commands[2])
    try:
        os.makedirs(patch, exist_ok=True)
    except FileNotFoundError:
        pass

    with CleanUpFile(commands[1]) as source_file:
        with MoveFile(patch, file_move) as target_file:
            target_file.write(source_file.read())
