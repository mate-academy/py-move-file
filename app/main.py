import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if not parts or parts[0] != "mv" or len(parts) != 3:
        return
    _, source_file, destination = parts
    if source_file == destination:
        return
    directory, file_name = os.path.split(destination)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(source_file, "r") as src, open(destination, "w") as dst:
        dst.write(src.read())
    try:
        os.remove(source_file)
    except IsADirectoryError:
        shutil.rmtree(source_file)
