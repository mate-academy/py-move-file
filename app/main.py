import os
from pathlib import Path


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "mv":
        raise Exception("Invalid syntax")

    operation, source_file, destination_file = command_parts

    if not os.path.exists(source_file):
        raise Exception(f"Source file {source_file} does not exist")

    if (destination_file.endswith(os.path.sep)
            or destination_file.endswith("/")):
        directory = destination_file.rstrip(os.path.sep + "/")
        filename = os.path.basename(source_file)
    else:
        directory, filename = os.path.split(destination_file)

    if not directory:
        first_file_rename = Path(source_file)
        first_file_rename.rename(destination_file)
        return None

    # os.makedirs(os.path.join(directory), exist_ok=True)
    current_dir = ""
    if directory:
        for part in directory.split("/"):
            if part:
                current_dir = os.path.join(current_dir, part)
                if not os.path.exists(current_dir):
                    os.mkdir(current_dir)

    full_destination = os.path.join(current_dir, filename)\
        if directory else filename
    with (open(source_file, "r", encoding="utf-8") as file_in,
          open(full_destination, "w") as file_out):
        file_out.write(file_in.read())
    os.remove(source_file)
    return None
