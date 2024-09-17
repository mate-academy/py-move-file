import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if parts[0] != "mv":
        raise ValueError("невідома команда")

    source = parts[1]
    destination = parts[2]

    if not os.path.isfile(source):
        raise FileNotFoundError(f"Файл {source} не знайдено")

    if destination.endswith("/"):
        file_name = os.path.basename(source)
        destination = os.path.join(destination, file_name)

    destination_dir = os.path.dirname(destination)
    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    shutil.move(source, destination)

    print(f"файл {source} переміщено до {destination}")
