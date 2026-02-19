import os
from typing import List


def move_file(command: str) -> None:
    parts: List[str] = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source_file, target_path = parts

    if source_file == target_path or not os.path.exists(source_file):
        return

    directory: str = os.path.dirname(target_path)

    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(source_file, "r") as file_in, open(target_path, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(source_file)
