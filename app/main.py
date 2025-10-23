import os


def move_file(command: str) -> None:
    """
    Moves a file from a source to a destination based on an 'mv' command.

    Creates destination directories if they do not exist.
    Removes the source file after a successful move.
    If the destination path ends with a separator ('/' or '\\'),
    the source file is moved into that directory with its original name.
    """
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    source_path = parts[1]
    dest_path = parts[2]

    # **ВИПРАВЛЕНО**: Обробляємо випадок, коли шлях призначення — це папка.
    if dest_path.endswith(("/", "\\")):
        # Створюємо повний шлях, додаючи ім'я вихідного файлу до папки.
        # os.path.basename(source_path) отримує ім'я файлу (напр., "file.txt")
        dest_path = os.path.join(dest_path, os.path.basename(source_path))

    if source_path == dest_path:
        return

    try:
        # Створюємо директорії для файлу призначення, якщо їх немає
        dest_directory = os.path.dirname(dest_path)
        if dest_directory:
            # exist_ok=True запобігає помилці, якщо папка вже існує
            os.makedirs(dest_directory, exist_ok=True)

        # **ВИПРАВЛЕНО**: Використовуємо бінарний режим ('rb', 'wb')
        # для підтримки будь-яких типів файлів (текст, зображення тощо).
        with open(source_path, "rb") as file_in:
            content = file_in.read()

        with open(dest_path, "wb") as file_out:
            file_out.write(content)

        os.remove(source_path)

    except FileNotFoundError:
        pass  # Ігноруємо, якщо вихідний файл не знайдено
    except IOError:
        # Ігноруємо інші помилки, пов'язані з доступом до файлів
        pass
