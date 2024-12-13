import os
import shutil


class InvalidCommandError(Exception):
    pass


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise InvalidCommandError(
            "Invalid move command. Please use 'mv source_file destination'"
        )
    _, source_file, destination = parts
    if source_file == destination:
        raise InvalidCommandError("Source and destination are the same.")
    directory, _ = os.path.split(destination)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(source_file, "r") as src, open(destination, "w") as dst:
        dst.write(src.read())
    try:
        os.remove(source_file)
    except IsADirectoryError:
        shutil.rmtree(source_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Source file '{source_file}' not found.")
