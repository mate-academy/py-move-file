import os
import shutil


def move_file(command: str) -> None:
    parts = command.strip().split(" ", 2)
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format")

    _, source, destination = parts

    if not os.path.exists(source):
        raise FileNotFoundError(f"The file {source} does not exist")

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    dir_path = os.path.dirname(destination)

    if dir_path:
        # Розбиваємо шлях на частини, без залежності від '/' або '\'
        path_parts = dir_path.replace("\\", "/").split("/")
        current_path = ""
        for part in path_parts:
            current_path = os.path.join(current_path, part)
            if os.path.exists(current_path):
                if os.path.isfile(current_path):
                    os.remove(current_path)
                    os.mkdir(current_path)
            else:
                os.mkdir(current_path)

    shutil.move(source, destination)
