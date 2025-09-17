import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        print("Invalid command")
        return
    source_file = parts[1]
    destination_file = parts[2]
    dest_dir = os.path.dirname(destination_file)  # отримуємо шлях до папки
    if dest_dir:  # якщо не пусто
        os.makedirs(dest_dir, exist_ok=True)
    try:
        with (open(source_file, "rb") as src,
              open(destination_file, "wb") as dst):
            dst.write(src.read())

        os.remove(source_file)
    except FileNotFoundError:
        print("File not found")
