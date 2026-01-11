import os.path
from os import makedirs


def move_file(command: str) -> None:
    command = command.split()
    if len(command) == 3:
        _, file_origin, file_to_create = command

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
