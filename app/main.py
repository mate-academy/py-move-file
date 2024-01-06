import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        print(
            "Error: Invalid command format. "
            "Use 'mv source_path destination_path'."
        )
        return

    source_path = parts[1]
    destination_path = parts[2]

    if not os.path.exists(source_path):
        print(f"Error: Source file '{source_path}' not found.")
        return

    if not destination_path:
        print("Error: Destination path is empty.")
        return

    is_directory = destination_path.endswith("/")

    if is_directory:
        destination_path = os.path.join(
            destination_path, os.path.basename(source_path)
        )

    destination_dir = os.path.dirname(destination_path)
    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir, exist_ok=True)

    try:
        shutil.copy2(source_path, destination_path)
        print(f"File '{source_path}' moved to"
              f" '{destination_path}' successfully.")
        os.remove(source_path)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except FileExistsError as e:
        print(f"Error: {e}")
