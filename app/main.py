from __future__ import annotations
import os
from io import TextIOWrapper


class FileMoveContext:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> TextIOWrapper:
        self.file = open(self.filename, "r")
        return self.file

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        os.remove(self.filename)


def move_file(command: str) -> None:
    arguments = command.split(" ")
    if len(arguments) > 0 and arguments[0] == "mv":
        if len(arguments) < 2:
            print("Missing first argument")
            return
        if len(arguments) < 3:
            print("Missing second argument")
            return
        else:
            dirname = os.path.dirname(arguments[2])
            if dirname and not os.path.exists(dirname):
                os.makedirs(dirname)

        with FileMoveContext(arguments[1]) as source_file:
            with open(arguments[2], "w") as new_file:
                new_file.write(source_file.read())
    else:
        print("Command not found")
