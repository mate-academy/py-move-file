import os
import shutil


def move_file(command: str) -> str:
    try:
        current_command, file, new_file = command.split()

        if current_command != "mv" or file == new_file:
            raise ValueError(
                "You gave bad command or u didn't give correct new_file name"
            )

        dir_path = os.path.dirname(new_file)

        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
        shutil.move(file, new_file)
    except (ValueError, FileNotFoundError, PermissionError) as message:
        return str(message)
