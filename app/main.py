import os
import shutil


def move_file(command: str) -> None:
    command_part = command.split()
    if len(command_part) != 3 or command_part[0] != "mv":
        return

    source_file = command_part[1]
    destination_path = command_part[2]

    if not os.path.isfile(source_file):
        return

    if destination_path.endswith("/"):
        os.makedirs(destination_path, exist_ok=True)
        destination_file = os.path.join(destination_path,
                                        os.path.basename(source_file))
    else:
        directory = os.path.dirname(destination_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        destination_file = destination_path

    shutil.move(source_file, destination_file)
