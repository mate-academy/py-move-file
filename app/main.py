import os
import shutil


def move_file(command: str) -> bool:
    try:
        command, file, new_file = command.split(" ")
        consist_directory = "/" in new_file

        if command != "mv":
            raise ValueError
        elif consist_directory:
            dir_path = os.path.dirname(new_file)

            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            shutil.move(file, new_file)
        elif file != new_file:
            os.rename(file, new_file)
    except (ValueError, FileNotFoundError, PermissionError):
        return False
    else:
        return True
