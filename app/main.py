import os
import shutil


def move_file(command: str) -> None:
    command_parts = command.split()
    name_to_copy = command_parts[1]
    new_file = command_parts[2]
    if new_file.endswith("/"):
        if not os.path.isdir(new_file):
            os.makedirs(new_file)
        new_file = os.path.join(new_file, os.path.basename(name_to_copy))
    else:
        dest_dir = os.path.dirname(new_file)
        if dest_dir and not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        shutil.move(name_to_copy, new_file)
