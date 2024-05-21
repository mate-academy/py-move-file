import os
import shutil


def move_file(command: str) -> None:
    command_split = command.split(" ")
    if len(command_split) != 3 or command_split[0] != "mv":
        raise ValueError("Invalid command format. "
                         "Expected: mv source_file target_path")
    old_file_name = command_split[1]
    path_and_name = command_split[2]

    target_dir, target_file = os.path.split(path_and_name)

    if target_dir:
        os.makedirs(target_dir, exist_ok=True)
        target_path = os.path.join(target_dir, target_file)
    else:
        target_path = target_file

    shutil.move(old_file_name, target_path)
