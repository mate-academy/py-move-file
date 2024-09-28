import os
from os import mkdir


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        return self

    def __exit__(self,
                 exc_type: object,
                 exc_value: object,
                 traceback: object) -> None:
        os.remove(self.filename)


def move_file(command: str) -> None:
    mode, current_location, expected_location = command.split()

    if mode != "mv" or current_location == expected_location:
        return

    expected_way = expected_location.split("/")
    current_location = os.path.join(*current_location.split("/"))
    expected_location = os.path.join(*expected_way)

    if len(expected_way) > 1:
        directory_way = expected_way[:-1]
        current_folder = ""
        for way in directory_way:
            current_folder = os.path.join(current_folder, way)
            try:
                mkdir(current_folder)
            except FileExistsError:
                pass

    with CleanUpFile(current_location):
        with (open(current_location, "r") as current_file,
              open(expected_location, "w") as expected_file):
            for line in current_file:
                expected_file.write(line)
