import os
from os import remove, makedirs


def move_file(command: str) -> None:
    command = command.split()
    if len(command) != 3 or command[0] != "mv":
        return
    mov, name = os.path.split(command[2])
    if mov:
        makedirs(mov, exist_ok=True)
    with open(command[1], "r") as first, open(command[2], "w") as second:
        second.write(first.read())
    remove(command[1])
