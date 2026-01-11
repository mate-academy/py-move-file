import os
import shutil


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 and command_parts[0] != "mv":
        raise ValueError("Invalid command format. "
                         "Usage: mv file.txt some_dir/new_file.txt")

    command_name, source_file, destination_file = command_parts

    if not os.path.exists(source_file):
        raise FileNotFoundError(f"Source file not found: {source_file}")

    destination_directory = os.path.dirname(destination_file)

    if destination_directory and not os.path.exists(destination_directory):
        os.makedirs(destination_directory, exist_ok=True)

    try:
        shutil.move(source_file, destination_file)
    except shutil.Error as e:
        raise shutil.Error(f"Error moving file: {e}")
    except Exception as e:
        raise e
