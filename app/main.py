import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    _, source, destination = parts

    # если пути совпадают — ничего не делаем
    if source == destination:
        return

    # читаем содержимое файла
    with open(source, "r", encoding="utf-8") as file:
        content = file.read()

    # проверяем: это директория или файл
    is_directory = destination.endswith("/")

    if is_directory:
        return  # по условию работаем только с файлами

    # выделяем путь и имя файла
    dir_path = os.path.dirname(destination)
    file_name = os.path.basename(destination)

    # создаём вложенные директории
    if dir_path:
        path_parts = dir_path.split("/")

        current_path = ""
        for part in path_parts:
            current_path = os.path.join(current_path, part)
            if not os.path.exists(current_path):
                os.mkdir(current_path)

    # записываем новый файл
    new_path = os.path.join(dir_path, file_name) if dir_path else file_name

    with open(new_path, "w", encoding="utf-8") as file:
        file.write(content)

    # удаляем исходный файл
    os.remove(source)
