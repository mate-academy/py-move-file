import os
import shutil


def move_file(command: str) -> None:
    source_file = None
    try:
        _, source_file, destination_path = command.split()

        if any(char in source_file + destination_path for char in '<>:"|?*'):
            raise ValueError("file name contains invalid characters")
        if "/" in destination_path or "\\" in destination_path:
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        shutil.move(source_file, destination_path)

    except FileNotFoundError:
        print(f"Error: The file '{source_file}' does not exist.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
