import os
from os import path, makedirs


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3:
        raise ValueError(f"{len(command_list)} != 3")
    if command_list[0] != "mv":
        raise NameError(f"No such command {command_list[0]}")
    if not path.exists(command_list[1]):
        raise FileNotFoundError(f"File {command_list[1]} not found")

    directory, new_file_name = path.split(command_list[2])
    file_name = command_list[1]

    if directory:
        makedirs(directory, exist_ok=True)
        new_file_name = directory + "/" + new_file_name

    with open(file_name, "r") as file_in, open(new_file_name, "w") as file_out:
        file_out.write(file_in.read())
    os.remove(file_name)
