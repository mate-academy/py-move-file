import os
import shutil


def move_file(command: str) -> str:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        print("Неправильний формат команди. "
              "Очікується: mv <вихідний_файл> <файл_призначення>")
        return

    source_file = parts[1]
    destination_path = parts[2]

    source_abs_path = os.path.abspath(source_file)
    destination_abs_path = os.path.abspath(destination_path)

    if source_abs_path == destination_abs_path:
        return

    if destination_path.endswith("/"):
        target_path = os.path.join(destination_path,
                                   os.path.basename(source_file))
    else:
        target_path = destination_path

    target_dir = os.path.dirname(target_path)
    if target_dir and not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)

    try:
        shutil.move(source_file, target_path)
    except FileNotFoundError:
        print(f"Помилка: Вихідний файл {source_file} не знайдено.")
        return
    except OSError as e:
        print(f"Виникла помилка при переміщенні файлу: {e}")
        return
