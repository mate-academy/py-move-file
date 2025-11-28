import os


def move_file(command: str) -> None:
    parts = command.split()

    # Перевірка форми команди
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Usage: mv <source> <destination>")

    _, src, dst = parts

    # Перевірка існування файлу
    if not os.path.isfile(src):
        raise FileNotFoundError(f"Source file '{src}' does not exist")

    # Якщо dst — директорія або закінчується на "/" → переміщення в папку
    if dst.endswith("/") or os.path.isdir(dst):
        os.makedirs(dst, exist_ok=True)
        dst = os.path.join(dst, os.path.basename(src))
    else:
        # Якщо в шляху до файлу є директорії → створюємо
        dir_path = os.path.dirname(dst)
        if dir_path:  # якщо не пустий
            os.makedirs(dir_path, exist_ok=True)

    # Копіюємо файл вручну
    with open(src, "rb") as f_src, open(dst, "wb") as f_dst:
        f_dst.write(f_src.read())

    # Видаляємо старий
    os.remove(src)
