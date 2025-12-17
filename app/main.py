import os
from logging import debug

from app.cleanup_manager import CleanUpFile


def move_file(command: str) -> None:
    operators = command.split(" ")
    if operators[0] != "mv":
        return

    if len(operators) != 3:
        return

    if operators[1] != operators[2]:
        try:
            with CleanUpFile(operators[1]):
                with open(operators[1], "r") as first:
                    if "/" in operators[2]:
                        create_directory_recursively(operators[2])
                    with open(operators[2], "w") as second:
                        second.write(first.read())
        except Exception as e:
            debug(e)


def create_directory_recursively(file_trace: str) -> None:
    dir_list = file_trace.split("/")
    temp_path = ""
    for i in dir_list[:-1]:
        if not os.path.exists(f"{temp_path}{i}"):
            os.mkdir(f"{temp_path}{i}")
        temp_path += i + "/"
