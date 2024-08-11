import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. "
                         "Use: mv source_file destination_path")

    _, source, destination = parts

    if not os.path.isfile(source):
        raise FileNotFoundError(f"No such file: '{source}'")

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        dir_path = os.path.dirname(destination)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

    os.rename(source, destination)
