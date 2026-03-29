import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source_path, destination_path = parts

    with open(source_path, "r", encoding="utf-8") as source_file:
        content = source_file.read()

    if destination_path.endswith("/") or destination_path.endswith("\\"):
        file_name = os.path.basename(source_path)
        destination_path = os.path.join(destination_path, file_name)

    destination_dir = os.path.dirname(destination_path)

    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    with open(destination_path, "w", encoding="utf-8") as destination_file:
        destination_file.write(content)

    os.remove(source_path)
