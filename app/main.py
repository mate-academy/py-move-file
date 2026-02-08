import os
from pathlib import Path


def move_file(command: str) -> None:
    command_parts = command.split()
    destination_file = ""
    if "/" not in command_parts[2]:
        with (open(command_parts[1], "r") as file_in,
              open(command_parts[2], "w") as file_out):
            file_out.write(file_in.read())
        os.remove(command_parts[1])
    if len(command_parts) == 3:
        path = command_parts[2].split("/")
        for item in path:
            if ".txt" in item:
                destination_file = item
                path.remove(item)
        path_to_file = Path(*path)
        os.makedirs(os.path.join(*path), exist_ok=True)
        with (open(command_parts[1], "r", encoding="utf-8") as file_in,
              open(f"{path_to_file}/{destination_file}", "w") as file_out):
            file_out.write(file_in.read())
        os.remove(command_parts[1])
