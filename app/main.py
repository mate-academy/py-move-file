import os
import shlex  # ## ПОКРАЩЕНО: Для надійного парсингу команд


def move_file(command: str) -> None:
    """
    Moves a file from a source to a destination based on an 'mv' command.

    This version correctly handles paths with spaces, differentiates between
    a file and a directory as a destination, and uses more precise
    error handling.
    """
    try:
        # ## ПОКРАЩЕНО: shlex.split коректно обробляє шляхи з пробілами
        parts = shlex.split(command)
    except ValueError:
        return  # Помилка парсингу, якщо, наприклад, незакриті лапки

    if len(parts) != 3 or parts[0] != "mv":
        return

    source_path = parts[1]
    dest_path = parts[2]

    # ## ПОКРАЩЕНО: Порівнюємо абсолютні шляхи для надійності
    if os.path.abspath(source_path) == os.path.abspath(dest_path):
        return

    # ## ПОКРАЩЕНО: Розумна обробка директорії як місця призначення
    if os.path.isdir(dest_path):
        dest_path = os.path.join(dest_path, os.path.basename(source_path))

    try:
        # ## ПОКРАЩЕНО: Більш точна обробка помилок
        # Ловимо FileNotFoundError тільки для вихідного файлу
        with open(source_path, "rb") as file_in:
            content = file_in.read()

        dest_directory = os.path.dirname(dest_path)
        if dest_directory:
            os.makedirs(dest_directory, exist_ok=True)
