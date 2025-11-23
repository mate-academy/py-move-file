from pathlib import Path
import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3:
        return

    if command_list[0] != "mv":
        return

    source_path = command_list[1]
    destination_path = command_list[2]

    if source_path == destination_path:
        return

    if not Path(source_path).is_file():
        return

    list_destination = destination_path.split("/")

    directory_path = ""
    for index in range(0, len(list_destination) - 1):
        directory_path += list_destination[index]

        if not Path(directory_path).is_dir():
            os.mkdir(directory_path)

        directory_path += "/"

    with (open(source_path, "r") as file_from,
          open(destination_path, "w") as file_to):
        file_to.write(file_from.read())

    if os.path.exists(destination_path):
        os.remove(source_path)
