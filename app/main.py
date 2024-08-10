import os
import shutil


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3:
        _, source_file, destination_file = command_list
        if not os.path.isdir(destination_file):
            if (os.path.dirname(destination_file)
                    == os.path.dirname(source_file)):
                os.rename(source_file, destination_file)
            else:
                os.makedirs(os.path.dirname(destination_file), exist_ok=True)
                shutil.move(source_file, destination_file)
