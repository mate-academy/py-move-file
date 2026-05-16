from __future__ import annotations
import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "mv":
        return

    source_file = command_parts[1]
    destination_path = command_parts[2]

    if destination_path.endswith("/"):
        directory_path = destination_path
        file_base_name = os.path.basename(source_file)
        destination_file = os.path.join(destination_path, file_base_name)
    else:
        directory_path = os.path.dirname(destination_path)
        destination_file = destination_path

    if source_file == destination_file:
        return

    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    with open(source_file, "r") as file_in:
        file_content = file_in.read()

    with open(destination_file, "w") as file_out:
        file_out.write(file_content)

    os.remove(source_file)
