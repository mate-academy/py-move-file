import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    cmd, source, destination = parts

    if cmd != "mv":
        return

    if source == destination:
        return

    # читаем файл
    with open(source, "r", encoding="utf-8") as file:
        content = file.read()

    # если путь заканчивается "/" → это директория
    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    # получаем директорию
    dir_path = os.path.dirname(destination)

    # создаём папки (cross-platform)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    # пишем новый файл
    with open(destination, "w", encoding="utf-8") as file:
        file.write(content)

    # удаляем старый файл
    os.remove(source)
