from __future__ import annotations
from typing import Type
import os
from traceback import TracebackException


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        if not os.path.exists(self.filename):
            raise ValueError("файлу нема")
        return self

    def __exit__(
            self,
            exc_type: Type[BaseException],
            exc_val: BaseException,
            exc_tb: TracebackException
    ) -> bool:
        os.remove(self.filename)
        return True

# with CleanUpFile("file.txt"):
#     with open("file.txt", "w") as file:
#         file.write("Hello Mate!")
