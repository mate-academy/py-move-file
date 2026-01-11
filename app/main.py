import os


def move_file(command: str) -> None:
    # Розділяємо команду на частини
    command_list = command.split()
    if len(command_list) != 3:
        raise ValueError("Invalid command format."
                         " Expected 'mv <source> <destination>'")

    # Витягуємо шляхи до вихідного та цільового файлів
    _, src, dst = command_list

    # Якщо ціль - це директорія (шлях закінчується '/')
    if dst.endswith("/"):
        # Додаємо ім'я вихідного файлу до цільової директорії
        dst = os.path.join(dst, os.path.basename(src))

    # Створюємо директорії, якщо вони не існують
    directory = os.path.dirname(dst)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)  # Створюємо всі необхідні директорії

    # Переміщаємо файл, використовуючи os.rename (аналог os.replace)
    os.rename(src, dst)
