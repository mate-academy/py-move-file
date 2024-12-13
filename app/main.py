import shutil
import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        print("Incorrect command.")

    _, source_file, destination_path = parts

    if not os.path.exists(source_file):
        print(f"Error: Source file '{source_file}' does not exist.")
        return

    if destination_path.endswith("/"):
        os.makedirs(destination_path, exist_ok=True)
        destination_path = os.path.join(destination_path,
                                        os.path.basename(source_file))
    else:
        parent_dir = os.path.dirname(destination_path)
        if parent_dir and not os.path.exists(parent_dir):
            os.makedirs(parent_dir, exist_ok=True)

    try:
        shutil.move(source_file, destination_path)
    except Exception as e:
        print(f"Error moving file: {e}")
