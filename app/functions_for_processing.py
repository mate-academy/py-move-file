from typing import TextIO
from contextlib import contextmanager
import os


def create_path(dir_list: list) -> None:
    for index in range(1, len(dir_list)):
        os.mkdir(os.path.join(*dir_list[:index]))


@contextmanager
def processing_files(
        name: str,
        method: str,
        to_delete: str,
        source: TextIO
) -> None:
    new_file = open(name, method)
    try:
        yield new_file
    finally:
        new_file.write(source.read())
        source.close()
        new_file.close()
        os.remove(f"{to_delete}")
