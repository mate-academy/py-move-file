import os
from typing import Any


class CleanUpFile:
    def __init__(
            self,
            filename: str
    ) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> Any:
        self.file = open(self.filename, "+r")
        return self.file

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.file.close()
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            pass


def copy_file(command: str) -> None:
    command_ls = command.split()
    if command_ls[1] == command_ls[2]:
        return
    with CleanUpFile(command_ls[1]) as source,\
         open(command_ls[2], "w") as receiver:
        source_contents = source.read()
        receiver.write(source_contents)


def move_file(command: str) -> None:
    destination = command.split()[2]
    if destination.count("/") == 1:
        directory = destination.split("/")[0]
        try:
            os.mkdir(directory)
        except FileExistsError:
            pass
    elif destination.count("/") > 1:
        directories = destination[:destination.rfind("/")]
        try:
            os.makedirs(directories)
        except FileExistsError:
            pass
    copy_file(command)
