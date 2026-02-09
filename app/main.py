import os
from pathlib import Path


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "mv":
        raise Exception("Invalid syntax")
    operation, source_file, destination_file = command_parts
    directory, filename = os.path.split(destination_file)
    if not directory:
        if not os.path.exists(source_file):
            raise Exception(f"Source file {source_file} does not exist")
        else:
            first_file_rename = Path(source_file)
            first_file_rename.rename(destination_file)
        return None

    os.makedirs(os.path.join(directory), exist_ok=True)
    with (open(source_file, "r", encoding="utf-8") as file_in,
          open(os.path.join(str(directory), filename), "w") as file_out):
        file_out.write(file_in.read())
    os.remove(source_file)
    return None
