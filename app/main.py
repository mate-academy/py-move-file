import os


def move_file(command: str) -> None:
    parts = command.strip().split()

    # Перевірка формату
    if len(parts) != 3 or parts[0] != "mv":
        print("❌ Invalid command format. Expected: mv source destination")
        return

    source_path = parts[1]
    destination_path = parts[2]

    # Перевірка, що файл існує
    if not os.path.exists(source_path):
        print(f"⚠️ Source path '{source_path}' does not exist.")
        return
    if not os.path.isfile(source_path):
        print(f"❌ Source '{source_path}' is not a file.")
        return

    # Обробка шляху призначення
    filename = os.path.basename(source_path)
    if destination_path.endswith("/") or os.path.isdir(destination_path):
        final_destination = os.path.join(destination_path, filename)
    else:
        final_destination = destination_path

    # Створення директорій для призначення
    dest_dir = os.path.dirname(final_destination)
    if dest_dir:
        parts = dest_dir.replace("\\", "/").split("/")
        current_path = "."
        for part in parts:
            current_path = os.path.join(current_path, part)
            if os.path.exists(current_path):
                if not os.path.isdir(current_path):
                    print(f"❌ Cannot create directory '{current_path}': path exists and is not a directory.")
                    return
            else:
                os.mkdir(current_path)

    # Переміщення файлу
    try:
        with open(source_path, "rb") as src:
            content = src.read()

        with open(final_destination, "wb") as dst:
            dst.write(content)

        os.remove(source_path)
        print(f"✅ File successfully moved to: {final_destination}")
    except OSError as e:
        print(f"❌ File operation failed: {e}")
