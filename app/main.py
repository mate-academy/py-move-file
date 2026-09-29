# write your code here
import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()

    # Валідація вхідних даних відповідно до вимог ментора
    if len(parts) != 3 or parts[0] != "mv":
        return

    # Використовуємо розпакування відповідно до [CHECKLIST ITEM 6]
    _, source, destination = parts

    # Обробка випадку, якщо призначення закінчується на '/'
    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    # Використовуємо os.path для сумісності відповідно до [CHECKLIST ITEM 4]
    directory = os.path.dirname(destination)

    # Перевіряємо існування папки вручну без exist_ok=True [CHECKLIST ITEM 2]
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    # Копіюємо вміст та використовуємо суворо os.remove() для видалення
    shutil.copyfile(source, destination)
    os.remove(source)
