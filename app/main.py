import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        print("Invalid command format. Use: mv source_file destination_path")
        return

    source_path = parts[1]
    destination_path = parts[2]

    try:
        if destination_path.endswith("/"):
            # Перевіряємо, чи вже існує директорія призначення
            if not os.path.exists(destination_path):
                os.makedirs(destination_path, exist_ok=True)
            destination_file = os.path.join(destination_path,
                                            os.path.basename(source_path))
            shutil.move(source_path, destination_file)
        else:
            destination_dir = os.path.dirname(destination_path)
            if destination_dir and not os.path.exists(destination_dir):
                os.makedirs(destination_dir, exist_ok=True)
            shutil.move(source_path, destination_path)
        print(f"Successfully moved '{source_path}' to '{destination_path}'")
    except FileNotFoundError:
        print(f"Error: Source file '{source_path}' not found.")
    except OSError as e:
        print(f"Error moving file: {e}")
