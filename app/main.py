import os


def move_file(command: str) -> None:
    # Парсинг команды: отделяем "mv" и пути
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Invalid command format. Use: mv <source> <destination>")

    source_path, destination_path = parts[1], parts[2]

    # Проверка, существует ли исходный файл
    if not os.path.isfile(source_path):
        raise FileNotFoundError(f"No such file: '{source_path}'")

    # Если destination заканчивается на "/", он является каталогом
    if destination_path.endswith("/"):
        os.makedirs(destination_path, exist_ok=True)
        destination_path = os.path.join(
            destination_path, os.path.basename(source_path))
    else:
        # Создаем промежуточные каталоги, если их нет
        destination_dir = os.path.dirname(destination_path)
        if destination_dir:
            os.makedirs(destination_dir, exist_ok=True)

    # Перемещаем файл
    with open(source_path, "rb") as src_file:
        content = src_file.read()

    with open(destination_path, "wb") as dest_file:
        dest_file.write(content)

    # Удаляем исходный файл
    os.remove(source_path)
