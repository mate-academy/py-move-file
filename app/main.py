import os


def move_file(command: str) -> str:

    parts = command.split()  # Парсинг команди.
    # Тобто розбиваємо рядок за пробілами на частини.
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Невірний формат команди")

    source = parts[1]  # файл, який потрібно перемістити
    destination = parts[2]  # шлях, куди переміщувати

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)  # створення директорії
        destination = os.path.join(destination, os.path.basename(source))
        # Додання ім’я лише вихідного файлу до даної директорії
        # (отримання повного шляху)
    directory = os.path.dirname(destination)
    # Це повертає шлях до директорії без імені файлу

    if directory:  # Якщо шлях існує -
        os.makedirs(directory, exist_ok=True)
        # - створюється вся структура директорій

    os.rename(source, destination)  # Файл source переміщується до destination.
    # Це одночасно копіює та видаляє оригінал
