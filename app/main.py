import shutil
import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) == 3 and command[0] == "mv":
        _, source_file, destination_path = command
        dir_path = os.path.dirname(destination_path)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
        if os.path.exists(destination_path):
            os.remove(destination_path)
        shutil.move(source_file, destination_path)
