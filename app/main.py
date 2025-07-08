import os


def move_file(command: str) -> None:
    parts = command.split(maxsplit=2)
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format")

    _, source_path, destination_path = parts

    if destination_path.endswith("/"):
        destination_path = os.path.join(
            destination_path, os.path.basename(source_path)
        )

    destination_dir = os.path.dirname(destination_path)

    if destination_dir:
        current_path = ""
        for folder in destination_dir.split(os.sep):
            current_path = os.path.join(current_path, folder)
            if current_path and not os.path.exists(current_path):
                os.mkdir(current_path)

    os.rename(source_path, destination_path)
