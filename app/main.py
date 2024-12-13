import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        raise ValueError("Invalid command format")

    mv, source_file, destination_file = parts

    if mv != "mv":
        raise ValueError("Command not found")

    destination_dir, new_file_name = os.path.split(destination_file)

    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    os.replace(source_file, os.path.join(destination_dir, new_file_name))
