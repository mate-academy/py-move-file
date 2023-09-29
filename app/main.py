import os
import shutil


def make_directories(destination_path: str) -> None:

    directories = destination_path.split(os.path.sep)
    current_path = ""

    for directory in directories:
        current_path = os.path.join(current_path, directory)

        if not os.path.exists(current_path):
            os.makedirs(current_path, exist_ok=True)


def move_file(command: str) -> None:
    parts = command.split()
    mv, source_path, destination_path = parts
    if len(parts) != 3 or mv != "mv":
        return

    if not os.path.exists(source_path):
        return

    is_directory = False
    if destination_path.endswith(os.path.sep):
        is_directory = True
        destination_path = destination_path.rstrip(os.path.sep)

    if is_directory:
        make_directories(destination_path)

    if is_directory:
        destination_file = os.path.join(destination_path, os.path.basename(source_path))
    else:
        destination_file = destination_path

    shutil.move(source_path, destination_file)
