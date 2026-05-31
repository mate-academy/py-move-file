import os
from pathlib import Path


def move_file(command: str) -> None:
    command = command.split()
    if command[0] != "mv" or len(command) != 3:
        return
    original_file = command[1]
    new_file = Path(command[2])
    new_file.parent.mkdir(parents=True, exist_ok=True)
    with open(original_file, "r") as o_file, open(new_file, "w") as n_file:
        n_file.write(o_file.read())
    os.remove(original_file)
