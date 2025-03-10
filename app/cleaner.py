from typing import Any
import os


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.filename = file_name
        self.file = None

    def __enter__(self) -> Any:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        os.remove(self.filename)
