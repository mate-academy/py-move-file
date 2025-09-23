import os


def move_file(command: str) -> None:
    """
    Move a file from source to destination like Linux 'mv' command.

    Args:
        command (str): command string, e.g. "mv file.txt dir/new_file.txt"
    """
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Command must be in format: mv source_file destination_path"
        )

    src = parts[1]
    dst = parts[2]

    # Якщо кінцевий шлях закінчується на '/', вважаємо його директорією
    if dst.endswith("/"):
        dst = os.path.join(dst, os.path.basename(src))

    dst_dir = os.path.dirname(dst)

    # Створюємо всі проміжні директорії, якщо їх не існує
    if dst_dir and not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    # Копіюємо вміст у нове місце
    with open(src, "r", encoding="utf-8") as f_src, \
         open(dst, "w", encoding="utf-8") as f_dst:
        f_dst.write(f_src.read())

    # Видаляємо оригінальний файл
    os.remove(src)
