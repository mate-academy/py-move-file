from __future__ import annotations
import os
from typing import Any


class MoveFileContext:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> Any:
        self.file = open(self.filename, "r")
        return self.file

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        if self.file:
            self.file.close()
        os.remove(self.filename)


def move_file(command: str) -> None:
    words = command.split(" ")

    dirname = os.path.dirname(words[2])

    if dirname and not os.path.exists(dirname):
        os.makedirs(dirname, exist_ok=True)

    with MoveFileContext(words[1]) as source_file:
        with open(words[2], "w") as new_file:
            new_file.write(source_file.read())