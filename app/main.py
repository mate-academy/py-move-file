import os
import shutil


def move_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) != 3 or command_split[0] != "mv":
        raise ValueError(f"Invalid command: {command}")
    _, source_file, new_file = command_split
    new_dir, new_filename = os.path.split(new_file)
    new_dir = os.path.abspath(new_dir)
    os.makedirs(new_dir, exist_ok=True)
    try:
        shutil.move(source_file, os.path.join(new_dir, new_filename))
    except OSError as error:
        raise OSError(f"Error moving file: {error}")
