import os


def move_file(command: str) -> None:
    parts = command.split()

    # Перевірка кількості елементів
    if len(parts) != 3:
        raise ValueError("Команда має бути: mv <source> <destination>")

    action, source, destination = parts

    # Перевірка першого елемента
    if action != "mv":
        raise ValueError("Команда повинна починатися з 'mv'")

    # Перевірка існування файлу-джерела
    if not os.path.isfile(source):
        raise FileNotFoundError(f"Файл-джерело '{source}' не існує")

    # Якщо destination закінчується на '/', додаємо ім’я файлу
    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    directory = os.path.dirname(destination)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(source)
