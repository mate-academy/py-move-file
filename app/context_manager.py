from os import remove, makedirs, path


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
            exc_type: str,
            exc_val: str,
            exc_tb: str
    ) -> None:
        remove(self.source_file_name)
