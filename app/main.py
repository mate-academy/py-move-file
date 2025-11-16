import os
from os import makedirs, path


def move_file(command: str) -> None:

    command_list = command.split(" ")

    destination_path = path.dirname(command_list[2])
    create_file_name = path.basename(command_list[2])
    result_path = create_file_name
    file_to_copy = command_list[1]

    if destination_path != "":
        makedirs(destination_path, exist_ok=True)

        result_path = path.join(destination_path, create_file_name)

    data = ""

    with open(file_to_copy, "r") as file:
        data = file.read()

    with open(result_path, "w") as file:
        file.write(data)

    os.remove(file_to_copy)
