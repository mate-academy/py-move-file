from os import remove, makedirs
import os.path as path
from types import TracebackType
from typing import Optional, Type


class MoveFileManager:
    def __init__(
            self,
            source_file_name: str,
            path_to_file: str
    ) -> None:
        self.source_file_name = source_file_name
        self.path_to_file = path_to_file

    def __enter__(self) -> None:
        if self.path_to_file and not path.exists(self.path_to_file):
            makedirs(self.path_to_file)

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[Type[BaseException]],
            exc_tb: Optional[TracebackType]
    ) -> None:
        remove(self.source_file_name)
