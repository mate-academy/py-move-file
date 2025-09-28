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
        if action == "mv" and os.path.exists(source_file):
            if not os.path.exists(destination):
                path = os.path.dirname(destination)
                if path:
                    os.makedirs(path, exist_ok=True)
            with (Cleaner(source_file)):
                with open(source_file, "r"
                          ) as source, open(destination, "w"
                                            ) as destination:
                    destination.write(source.read())



def move_file1(command: str) -> None:
    parts = command.split()
    if len(parts) == 3:
        action, source_file, destination = parts
        if action == "mv" and os.path.exists(source_file):
            if not os.path.exists(destination):
                path = os.path.dirname(destination)
                if path:
                    current = None
                    for folder in path.split("/"):
                        if current is None:
                            os.mkdir(folder)
                            current = folder
                        else:
                            os.mkdir(current + "/" + folder)
                            current += "/" + folder
            with (Cleaner(source_file)):
                with open(source_file, "r"
                          ) as source, open(destination, "w"
                                            ) as destination:
                    destination.write(source.read())

print(move_file1("mv file.txt first_dir/second_dir/third_dir/file2.txt"))