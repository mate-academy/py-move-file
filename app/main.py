import os


def move_file(command: str) -> None:
    # Розділяємо команду на частини
    parts = command.strip().split()

    # Валідація формату команди
    if len(parts) != 3 or parts[0] != "mv":
        print("❌ Invalid command format. Expected: mv source destination")
        return

    source = parts[1]
    destination = parts[2]

    # Перевірка наявності джерела
    if not os.path.exists(source):
        print(f"⚠️ Source path '{source}' does not exist.")
        return

    # Перевірка, що джерело — саме файл
    if not os.path.isfile(source):
        print(f"❌ Source '{source}' is not a file.")
        return

    # Визначення імені файлу
    filename = os.path.basename(source)

    # Якщо destination закінчується на / або є директорією, додаємо ім'я файлу
    if destination.endswith("/") or os.path.isdir(destination):
        final_destination = os.path.join(destination, filename)
    else:
        final_destination = destination

    # Створюємо потрібні директорії, якщо їх немає
    dest_dir = os.path.dirname(final_destination)
    if dest_dir and not os.path.exists(dest_dir):
        try:
            os.makedirs(dest_dir)
        except OSError as e:
            print(f"❌ Failed to create directory '{dest_dir}': {e}")
            return

    # Копіювання і видалення
    try:
        with open(source, "rb") as src_file, open(final_destination, "wb") as dst_file:
            dst_file.write(src_file.read())
        os.remove(source)
        print(f"✅ File successfully moved to: {final_destination}")
    except OSError as e:
        print(f"❌ File operation failed: {e}")
