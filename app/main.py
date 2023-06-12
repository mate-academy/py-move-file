import os
import shutil


def move_file(command: str) -> str:
    try:
        current_command, file, new_file = command.split()

        if current_command != "mv" or file == new_file:
            raise ValueError

        consist_directory = "/" in new_file

        if consist_directory:
            dir_path = os.path.dirname(new_file)

            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            shutil.move(file, new_file)
        else:
            os.rename(file, new_file)
    except (ValueError, FileNotFoundError, PermissionError) as message:
        return str(message)
