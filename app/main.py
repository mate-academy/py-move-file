from __future__ import annotations
import os
from typing import Any


class MoveFile:
    def __init__(
            self,
            old_filename: str,
            new_filename: str,
            direction: str
    ) -> None:
        self.old_filename = old_filename
        self.new_filename = new_filename
        self.direction = direction

    def __enter__(self) -> MoveFile:
        self.new_filename = open(f"{self.direction}/{self.new_filename}", "w")
        with open(self.old_filename, "r") as f:
            content_to_copy = f.read()
        self.new_filename.write(content_to_copy)
        return self.new_filename

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        os.remove(self.old_filename)
        self.new_filename.close()


def move_file(command: str) -> None:
    content = command.split()
    if len(content) == 3:
        command, old_file, new_file_and_direction = content
        if command == "mv":
            direction, new_file_name = os.path.split(new_file_and_direction)
            if direction:
                if not os.path.exists(direction):
                    os.makedirs(direction, exist_ok=True)
            else:
                direction = os.getcwd()

            with MoveFile(old_file, new_file_name, direction):
                pass
