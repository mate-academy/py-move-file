import os
import shutil


def move_file(command: str) -> None:
    splitted_command = command.split()
    if len(splitted_command) != 3 or splitted_command[0] != "mv":
        raise ValueError

    source_path = splitted_command[1]
    destination_path = splitted_command[2]

    if not os.path.isfile(source_path):
        raise FileNotFoundError

    if not source_path.strip() or not destination_path.strip():
        raise ValueError

    source_path = os.path.abspath(source_path)
    destination_path = os.path.abspath(destination_path)

    if destination_path.endswith(os.path.sep):
        destination_path = os.path.join(destination_path,
                                        os.path.basename(source_path))

    destination_dir = os.path.dirname(destination_path)

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    shutil.move(source_path, destination_path)
