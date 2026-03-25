import os
from pathlib import Path


def move_file(command_request: str) -> None:
    command_list = command_request.split(" ")

    if len(command_list) == 3:
        command, source_path, destination_path = command_list

        if os.path.isdir(destination_path):
            destination_path += os.path.basename(source_path)

        if command == "mv":
            make_dirs(
                Path(os.path.dirname(destination_path))
            )

            with (open(source_path, "r") as source_file_object,
                  open(destination_path, "w") as destination_file_object):
                destination_file_object.write(source_file_object.read())
            os.remove(source_path)


def make_dirs(dir_path: Path) -> None:
    dirs_list = dir_path.parts
    current_path = ""
    for dir_index in range(len(dirs_list)):
        current_path = os.path.join(current_path, dirs_list[dir_index])
        print(current_path)
        if not os.path.isdir(current_path):
            os.mkdir(current_path)
