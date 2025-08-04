import os
import shutil


def move_file(command: str) -> None:
    parts = command.strip().split()

    if len(parts) != 3 or parts[0] != "mv":
        return  # некоректна команда

    src, dst = parts[1], parts[2]

    # Якщо шлях закінчується на '/', вважаємо це директорією — додаємо ім'я файла
    if dst.endswith("/"):
        dst = os.path.join(dst, os.path.basename(src))

    # Створюємо всі проміжні директорії, якщо їх ще не існує
    dst_dir = os.path.dirname(dst)
    if dst_dir and not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    # Переміщаємо файл і видаляємо оригінал
    shutil.copy2(src, dst)
    os.remove(src)
