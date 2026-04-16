import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    source = parts[1]
    destination = parts[2]

    if source == destination:
        return

    # Визначаємо шлях до папки
    if destination.endswith("/"):
        directory = destination
        destination_path = os.path.join(destination, os.path.basename(source))
    else:
        directory = os.path.dirname(destination)
        destination_path = destination

    # Створюємо директорії будь-якої вкладеності
    if directory:
        os.makedirs(directory, exist_ok=True)

    try:
        with open(source, "r", encoding="utf-8") as file_in:
            content = file_in.read()

        with open(destination_path, "w", encoding="utf-8") as file_out:
            file_out.write(content)

        os.remove(source)
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    # Щоб не було IndentationError, тут має бути код або pass
    pass
