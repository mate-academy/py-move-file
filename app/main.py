import os
import shutil


def move_file(command: str) -> None:
    command_name, source_file, destination_file = command.split()
    source_directory = os.path.dirname(source_file)
    destination_directory = os.path.dirname(destination_file)

    if source_directory == destination_directory:
        os.rename(source_file, destination_file)
    else:
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)

        shutil.move(source_file, destination_file)
