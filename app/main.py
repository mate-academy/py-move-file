import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. "
                         "Use: mv source_path destination_path")

    source_path = parts[1]
    destination_path = parts[2]

    if not os.path.isfile(source_path):
        raise FileNotFoundError(f"No such file: '{source_path}'")

    if destination_path.endswith("/"):
        raise ValueError("Destination path should not end with '/'")

    dest_dir = os.path.dirname(destination_path)

    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    os.rename(source_path, destination_path)
