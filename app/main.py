import os
import shutil


def move_file(command: str) -> None:

    parts = command.split()
    source = parts[1]
    destination = parts[2]

    if destination.endswith("/"):
        final_destination = os.path.join(destination, os.path.basename(source))
        os.makedirs(destination, exist_ok=True)
    else:

        final_destination = destination
        destination_dir = os.path.dirname(final_destination)
        if destination_dir:
            os.makedirs(destination_dir, exist_ok=True)

    try:
        shutil.copyfile(source, final_destination)
        os.remove(source)
        print(f"Файл '{source}' успішно переміщено в '{final_destination}'")
    except FileNotFoundError:
        print(f"Помилка: Файл '{source}' не знайдено.")
