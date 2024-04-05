import os
import shutil


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3:
        raise ValueError("Invalid command format. "
                         "Usage: mv file.txt some_dir/new_file.txt")

    command_name, source_file, destination_file = command_parts

    if len(command_parts) != 3:
        raise ValueError("Invalid move command format")

    if not os.path.exists(source_file):
        raise FileNotFoundError(f"Source file not found: {source_file}")

    source_directory = os.path.dirname(source_file)
    destination_directory = os.path.dirname(destination_file)

    if source_directory == destination_directory:
        os.rename(source_file, destination_file)
    else:
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)

        try:
            shutil.move(source_file, destination_file)
        except shutil.Error as e:
            raise shutil.Error(f"Error moving file: {e}")
        except Exception as e:
            raise e
