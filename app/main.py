import os
import shutil


def move_file(command: str) -> None:
    if command.strip().count(" ") == 2 and command.strip()[:3] == "mv ":
        _, current_file, new_file_path = command.strip().split()
        if os.path.exists(current_file):
            if os.path.split(new_file_path)[:-1][0]:
                os.makedirs(os.path.split(new_file_path)[:-1][0],
                            exist_ok=True)
            shutil.move(current_file, new_file_path)
