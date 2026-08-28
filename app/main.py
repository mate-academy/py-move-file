import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format")

    _, source, destination = parts

    destination = os.path.normpath(destination)
    destination_dir = os.path.dirname(destination)

    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir, exist_ok=True)

    with open(source, "r", encoding="utf-8") as src_file:
        content = src_file.read()

    with open(destination, "w", encoding="utf-8") as dest_file:
        dest_file.write(content)

    os.remove(source)
