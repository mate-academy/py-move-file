import os
import shutil


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3:
        raise ValueError("Invalid command format")

    operation, source_file, destination = command_parts

    if operation != "mv":
        raise ValueError("Invalid operation. Use 'mv' to move files.")

    if not os.path.isfile(source_file):
        raise FileNotFoundError(f"Source file '{source_file}' not found.")

    if os.path.isdir(destination):
        destination = os.path.join(destination, os.path.basename(source_file))

    destination_folder = os.path.dirname(destination)
    if destination_folder:
        os.makedirs(destination_folder, exist_ok=True)

    try:
        shutil.copy2(source_file, destination)
        os.remove(source_file)
        print(f"File moved to {destination}")

        with open(destination, "r") as file:
            print(file.read())

    except (PermissionError, FileNotFoundError) as e:
        print(f"Error: {e}")
    except Exception:
        print("An unexpected error occurred.")
