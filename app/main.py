import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Невірний формат команди.")

    _, source, destination = parts

    if not os.path.exists(source):
        raise FileNotFoundError(f"Файл {source} не знайдено")

    destination_dir = os.path.dirname(destination)
    destination_file = os.path.basename(destination)

    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    new_file_path = os.path.join(destination_dir, destination_file)
    shutil.move(source, new_file_path)
