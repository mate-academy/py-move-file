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
    if commands[0] != "mv":
        return
    if commands[1] == "" or commands[1] == "":
        return

    previous_dir = ""
    for directory in commands[2].split("/")[:-1]:
        if not os.path.isdir(os.path.join(previous_dir, directory)):
            os.mkdir(os.path.join(previous_dir, directory))
        previous_dir += directory + "/"

    with CleanUpFile(commands[1]) as source_file:
        with open(commands[2], "w") as target_file:
            target_file.write(source_file.read())
