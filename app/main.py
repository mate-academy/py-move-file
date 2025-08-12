import os
from typing import Optional


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source_file_name, destination_path = parts

    # Якщо шлях призначення закінчується "/", додаємо ім'я вихідного файлу
    if destination_path.endswith("/"):
        destination_path = os.path.join(destination_path, os.path.basename(source_file_name))

    # Створюємо необхідні папки
    destination_dir = os.path.dirname(destination_path)
    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    # Копіюємо вміст
    with open(source_file_name, "r", encoding="utf-8") as src, \
            open(destination_path, "w", encoding="utf-8") as dst:
        dst.write(src.read())

    # Видаляємо початковий файл
    os.remove(source_file_name)
