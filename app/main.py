import os
from pathlib import Path


def move_file(command: str) -> None:
    new_command = command.split()
    if len(new_command) != 3 or new_command[0] != "mv":
        return None
    path_of_source_file = new_command[1]
    path_of_destiny = new_command[2]

    if path_of_destiny.endswith(os.sep) or (
            os.altsep and path_of_destiny.endswith(os.altsep)
    ):
        name_start = os.path.basename(path_of_source_file)
        way = os.path.join(path_of_destiny, name_start)
    else:
        way = path_of_destiny

    current_path = os.path.dirname(way)

    path = Path(current_path)
    anchor = path.anchor
    parts = path.parts

    beginning = os.path.abspath(path_of_source_file)
    destination = os.path.abspath(way)

    if beginning == destination:
        return None

    current_dir = anchor
    new_parts = parts[1:] if anchor else parts

    for directory in new_parts:
        current_dir = os.path.join(current_dir, directory)

        if not os.path.exists(current_dir):
            os.mkdir(current_dir)

    with open(path_of_source_file, "r") as file_in, open(way, "w") as file_out:
        content = file_in.read()
        file_out.write(content)

    os.remove(path_of_source_file)
