import os
import shlex  # Для надійного парсингу команд з пробілами


def move_file(command: str) -> None:
    """
    Moves a file from a source to a destination based on an 'mv' command.

    This version handles paths with spaces, correctly interprets
    destination directories (even if they don't exist yet but end with '/'),
    copies in chunks (safe for large files), and uses more precise
    error handling.
    """
    try:
        parts = shlex.split(command)
    except ValueError:
        print("Error: Invalid command format.")
        return

    if len(parts) != 3 or parts[0] != "mv":
        return

    source_path = parts[1]
    dest_path = parts[2]

    # ## ПОКРАЩЕНО: (Критика 1)
    # Перевіряємо, чи шлях призначення є директорією.
    # Це правда, якщо шлях ВЖЕ існує і є папкою,
    # АБО якщо він ще не існує, але ЗАКІНЧУЄТЬСЯ на роздільник.
    final_dest_path = dest_path
    if (
        dest_path.endswith(("/", "\\"))
        or os.path.isdir(dest_path)
    ):
        final_dest_path = os.path.join(
            dest_path, os.path.basename(source_path)
        )

    # ## ПОКРАЩЕНО: (Критика 2)
    # Порівнюємо абсолютні шляхи *після* визначення фінального шляху.
    if os.path.abspath(source_path) == os.path.abspath(final_dest_path):
        return

    try:
        # ## ПОКРАЩЕНО: (Критика 3)
        # Блок 'try' для читання, щоб ловити FileNotFoundError.
        with open(source_path, "rb") as file_in:

            # Створюємо директорії лише якщо впевнені, що можемо читати.
            dest_directory = os.path.dirname(final_dest_path)
            if dest_directory:
                os.makedirs(dest_directory, exist_ok=True)

            # ## ПОКРАЩЕНО: (Критика 4)
            # Копіюємо блоками, щоб уникнути переповнення пам'яті.
            with open(final_dest_path, "wb") as file_out:
                while True:
                    chunk = file_in.read(8192)  # Читаємо блоками по 8KB
                    if not chunk:
                        break
                    file_out.write(chunk)

        # Видаляємо оригінал лише після успішного копіювання
        os.remove(source_path)

    except FileNotFoundError:
        # Обробляємо *тільки* відсутність вихідного файлу
        print(f"Error: Source file not found: {source_path}")
    except IOError as e:
        # Обробляємо інші помилки (напр., "Permission denied")
        print(f"Error during file operation: {e}")
