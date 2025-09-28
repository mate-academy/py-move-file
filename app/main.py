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
        os.remove(self.name)


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3:
        action, source_file, destination = parts
        if os.path.exists(source_file):
            if not os.path.exists(destination):
                path = os.path.dirname(destination)
                if path:
                    os.makedirs(path, exist_ok=True)
            with (Cleaner(source_file)):
                with open(source_file, "r"
                          ) as source, open(destination, "w"
                                            ) as destination:
                    destination.write(source.read())
