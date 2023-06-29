import os
from shutil import copyfile


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 and command_parts[0] != "mv":
        raise ValueError(
            "The command must be in the following format: "
            "'mv file.txt some_path/new_file.txt'"
        )

    _, old_file_name, new_file_path = command.split()
    directories_path, new_file_name = os.path.split(new_file_path)

    if directories_path:
        os.makedirs(directories_path, exist_ok=True)
        copyfile(old_file_name, os.path.join(directories_path, new_file_name))
        os.remove(old_file_name)
    else:
        os.rename(old_file_name, new_file_name)
