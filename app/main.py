import os


def move_file(command: str) -> None:

    parts = command.strip().split()

    # 1️⃣ Формат команди
    if len(parts) != 3 or parts[0] != "mv":
        print("❌ Invalid command format. Expected: mv source destination")
        return

    src = parts[1]
    dst = parts[2]

    # 2️⃣ Джерело існує і це саме файл
    if not os.path.exists(src):
        print(f"⚠️ Source path '{src}' does not exist.")
        return
    if not os.path.isfile(src):
        print(f"❌ Source '{src}' is not a file.")
        return

    # 3️⃣ Куди переміщаємо
    filename = os.path.basename(src)
    if dst.endswith("/") or os.path.isdir(dst):
        final_dst = os.path.join(dst, filename)
    else:
        final_dst = dst

    # 4️⃣ Створюємо всі необхідні директорії, але
    #    перевіряємо, чи якась з них не «зайнята» файлом
    dest_dir = os.path.dirname(final_dst)
    if dest_dir:
        curr = "."
        for part in dest_dir.replace("\\", "/").split("/"):
            curr = os.path.join(curr, part)
            if os.path.exists(curr):
                if not os.path.isdir(curr):
                    print(
                        f"❌ Cannot create directory '{curr}': "
                        "path exists and is not a directory."
                    )
                    return
            else:
                os.mkdir(curr)

    # 5️⃣ Копіюємо й видаляємо оригінал
    try:
        with open(src, "rb") as f_src, open(final_dst, "wb") as f_dst:
            f_dst.write(f_src.read())
        os.remove(src)
        print(f"✅ File successfully moved to: {final_dst}")
    except OSError as err:
        print(f"❌ File operation failed: {err}")
