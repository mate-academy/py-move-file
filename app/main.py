from __future__ import annotations
from typing import Any
import os


class ClearFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> ClearFile:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        os.remove(self.filename)


def move_clear_file(command: str, file_path1: str, file_path2: str) -> None:
    if command == "mv":
        try:
            with ClearFile(file_path1):
                with (
                    open(file_path1, "r") as file_in,
                    open(file_path2, "w") as file_out
                ):
                    file_out.write(file_in.read())
        except FileNotFoundError:
            print(f"FileNotFoundError:"
                  f" [WinError 2] Cannot find specified file: '{file_path1}'")


def move_file(command: str) -> None:
    command, file_path_name1, file_path_name2 = command.split()
    path = os.path.join(file_path_name2)
    path_catalog = path.split("/")
    if path[-1] != "/":
        creating_dir = []
        for current_dir in path_catalog[:-1]:
            creating_dir.append(current_dir)
            if not os.path.isdir("/".join(creating_dir)):
                os.mkdir("/".join(creating_dir))

        if os.path.isdir("/".join(path_catalog[:-1])):
            move_clear_file(command, file_path_name1, file_path_name2)

    if len(path.split("/")) == 1:
        move_clear_file(command, file_path_name1, file_path_name2)
