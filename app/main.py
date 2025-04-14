import os
import sys


def move_file(command: str) -> None:
    """
    Переміщує файл з одного місця в інше, подібно до команди mv в Unix.

    Команда має бути у форматі:
    "mv source destination"

    Якщо destination закінчується символом "/", то він розглядається як
    директорія, і файл буде переміщено в неї з використанням його початкового
    імені. Функція створює проміжні директорії за потребою і видаляє
    вихідний файл після переміщення.

    Args:
        command (str): Команда переміщення.
    """
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "mv":
        raise ValueError("Invalid command format.")

    source_path = command_parts[1]
    destination_input = command_parts[2]
    if destination_input.endswith("/"):
        destination_path = os.path.join(
            destination_input, os.path.basename(source_path)
        )
    else:
        destination_path = destination_input

    destination_dir = os.path.dirname(destination_path)
    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir, exist_ok=True)

    with open(source_path, "rb") as source_file:
        content = source_file.read()
    with open(destination_path, "wb") as destination_file:
        destination_file.write(content)
    os.remove(source_path)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: python script.py mv <source> <destination>"
        )
        sys.exit(1)
    move_file(" ".join(sys.argv[1:]))
    
