import os
import shutil


def move_file(command: str) -> None:
    splitted_command = command.split()

    if len(splitted_command) < 3:
        print(f"Incorrect command {command}")
        return

    init_file = splitted_command[1]
    new_file_directory_with_name = splitted_command[2]
    new_file_directory = os.path.dirname(new_file_directory_with_name)

    if not os.path.exists(init_file):
        print(f"File: '{init_file}' isn't exist.")
        return

    try:
        os.makedirs(new_file_directory)
        shutil.move(init_file, new_file_directory_with_name)
        print(f"File was moved to directory: {new_file_directory_with_name}")
    except OSError as error:
        shutil.move(init_file, new_file_directory_with_name)
        print(f"Error: {error}")
