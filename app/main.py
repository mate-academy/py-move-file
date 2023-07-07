import os
from pathlib import Path


def move_file(command: str) -> None:
    paths = command.split()[1:]
    file_name = paths[0]
    destination_path = paths[1].split("/")
    new_file = destination_path[-1]

    if not os.path.exists(file_name):
        print(f"File '{file_name}' does not exist.")
        return

    if "/" in command:
        des = "/".join(destination_path[:-1])

        Path(des).mkdir(parents=True, exist_ok=True)

        with open(file_name, "r") as file_1, open(
            des + "/" + str(new_file), "w"
        ) as file_2:
            file_2.write(file_1.read())

    else:
        with open(file_name, "r") as file_1, open(
            str(new_file), "w"
        ) as file_2:
            file_2.write(file_1.read())

    os.remove(file_name)
