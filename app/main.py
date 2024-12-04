import os
from typing import Any


def move_file(command: str) -> Any:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError

    word_in = parts[1]
    word_out = parts[2]

    if word_out[-1] == "/":
        word_out += word_in.split("/")[-1]
    directories = "/".join(word_out.split("/")[:-1])
    if directories:
        os.makedirs(directories, exist_ok=True)

    with open(word_in, "r") as file_in, open(word_out, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(word_in)
