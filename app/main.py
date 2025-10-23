import os


def move_file(command: str) -> None:
    """
    Moves a file from a source to a destination based on an 'mv' command.

    Creates destination directories if they do not exist.
    Removes the source file after a successful move.
    """
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    source_path = parts[1]
    dest_path = parts[2]

    if source_path == dest_path:
        return

    try:
        # 1. Створюємо директорії для файлу призначення, якщо їх немає
        dest_directory = os.path.dirname(dest_path)
        if dest_directory and not os.path.exists(dest_directory):
            # os.makedirs створює всі проміжні папки
            os.makedirs(dest_directory)

        # 2. Читаємо вміст вихідного файлу
        with open(source_path, "r") as file_in:
            content = file_in.read()

        # 3. Записуємо вміст у файл призначення
        with open(dest_path, "w") as file_out:
            file_out.write(content)

        # 4. Видаляємо вихідний файл після успішного копіювання
        os.remove(source_path)

    except FileNotFoundError:
        # Якщо вихідний файл не знайдено, нічого не робимо
        pass
