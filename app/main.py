import os
from typing import Optional, Type
from types import TracebackType


class MoveFile:
    def __init__(self, command: str) -> None:
        self.command = command
        self.source_file = None
        self.dest_file = None

    def __enter__(self) -> None:
        _, source_path, dest_path = self.command.split()
        dest_dir = os.path.dirname(dest_path)

        if dest_dir:
            os.makedirs(dest_dir, exist_ok=True)

        self.source_file = open(source_path, "r")
        self.dest_file = open(dest_path, "w")
        self.dest_file.write(self.source_file.read())

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType]
    ) -> None:
        if self.source_file:
            self.source_file.close()
        if self.dest_file:
            self.dest_file.close()

        if not exc_type:
            os.remove(self.command.split()[1])


def move_file(command: str) -> None:
    with MoveFile(command):
        pass


if __name__ == "__main__":
    move_file("mv file.txt file2.txt")
