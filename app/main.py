import os
import sys


def move_file(command: str) -> None:
    """
    Переміщує файл з одного місця в інше, подібно до команди mv в Unix.

    Команда має бути у форматі:
    "mv source destination"

    Якщо destination закінчується символом "/", то він розглядається як
    директорія, і файл буде переміщено в неї з використанням його початкового
    імені. Функція створює проміжні директорії за потребою і видаляє
    вихідний файл після переміщення.

    Args:
        command (str): Команда переміщення.
    """
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format.")
    src = parts[1]
    dest_input = parts[2]
    if dest_input.endswith("/"):
        dest = os.path.join(dest_input, os.path.basename(src))
    else:
        dest = dest_input

    dest_dir = os.path.dirname(dest)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir, exist_ok=True)

    with open(src, "rb") as src_file:
        content = src_file.read()
    with open(dest, "wb") as dest_file:
        dest_file.write(content)
    os.remove(src)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py mv <src> <dest>")
        sys.exit(1)
    # Формуємо команду типу "mv file.txt dest_path"
    move_file(" ".join(sys.argv[1:]))
