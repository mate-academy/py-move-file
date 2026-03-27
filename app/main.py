import os
import shutil


def move_file(command: str) -> None:
    commands = command.split()
    old_file_name, path_and_name = commands[1:]
    target_dir, target_file = os.path.split(path_and_name)
    if target_dir:
        os.makedirs(target_dir, exist_ok=True)
        target_path = os.path.join(target_dir, target_file)
    else:
        target_path = target_file
    shutil.move(old_file_name, target_path)
