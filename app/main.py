import os
from typing import List


def build_path(file_names: List[str]) -> str:
    path = ""
    for index, name in enumerate(file_names):
        if name.find(".") == -1:
            path += f"{name}/"
    return path


def move_file(command: str) -> None:
    divided_command = command.split()
    if not divided_command:
        return
    user_command = divided_command[0]

    if user_command == "mv" and len(divided_command) == 3:
        source_filename = divided_command[1]
        target_file_location = divided_command[2]

        source_file = open(source_filename, "r")

        if target_file_location.find("/") != -1:
            file_names = target_file_location.split("/")
            path = build_path(file_names)
            os.makedirs(path, exist_ok=True)

        with open(target_file_location, "w") as file_out:
            file_out.write(source_file.read())

        os.remove(source_filename)
