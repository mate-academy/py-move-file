from os import remove, makedirs, path
from types import TracebackType
from typing import Optional, Type


class MoveFileManager:
    def __init__(
            self,
            source_file_name: str,
            path: str
    ) -> None:
        self.source_file_name = source_file_name
        self.path = path

    def __enter__(self) -> None:
        if self.path and not path.exists(self.path):
            makedirs(self.path)

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[Type[BaseException]],
            exc_tb: Optional[TracebackType]
    ) -> None:
        remove(self.source_file_name)
