import os.path
from os import makedirs


def move_file(command: str) -> None:
    if len(command.split(" ")) == 3:
        list_command = command.split(" ")[1:]
        file_origin, file_to_create = list_command

    if os.path.dirname(file_to_create):
        with open(file_origin) as f_origin:
            file_data = f_origin.read()

        destination = os.path.dirname(file_to_create)
        makedirs(destination, exist_ok=True)

        with open(file_to_create, "w") as f_target:
            f_target.write(file_data)

        os.remove(file_origin)
    else:
        os.rename(file_origin, file_to_create)
