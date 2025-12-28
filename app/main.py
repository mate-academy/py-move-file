from __future__ import annotations
from types import TracebackType
from typing import Optional, Type
import os


class Cleaner:
    def __init__(self, name: str) -> None:
        self.name = name

    def __enter__(self) -> Cleaner:
        return self

    def __exit__(self,
                 exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[TracebackType]
                 ) -> None:
        if exc_type is None:
            os.remove(self.name)


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        raise ValueError
    action, source_file, destination_file = parts
    if action != "mv":
        raise ValueError
    if not os.path.isfile(source_file):
        raise ValueError
    if destination_file.endswith("/"):
        destination_file = os.path.join(destination_file,
                                        os.path.basename(source_file))
    path = os.path.dirname(destination_file)
    if path:
        current = ""
        for folder in os.path.normpath(path).split(os.path.sep):
            current = os.path.join(current, folder) \
                if current else folder
            if not os.path.exists(current):
                os.mkdir(current)
    with ((Cleaner(source_file))):
        with open(source_file, "rb") as source, \
            open(destination_file, "wb"
                 ) as destination:
            destination.write(source.read())
