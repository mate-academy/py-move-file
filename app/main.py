from os import path, makedirs, remove
from shutil import move


def make_directories(destination_path: str) -> None:

    directories = destination_path.split("/")
    current_path = ""

    for directory in directories:
        current_path = path.join(current_path, directory)
        if not path.exists(current_path):
            os.makedirs(current_path)


def move_file(command: str) -> None:
    parts = command.split()
    mv, source_path, destination_path = parts
    if len(parts) != 3 or mv != "mv":
        return

    if not path.exists(source_path):
        return

    is_directory = False
    if destination_path.endswith("/"):
        is_directory = True
        destination_path = destination_path.rstrip("/")

    if is_directory:
        make_directories(destination_path)

    if is_directory:
        destination_file = path.join(destination_path, path.basename(source_path))
    else:
        destination_file = destination_path

    move(source_path, destination_file)
    remove(source_path)
