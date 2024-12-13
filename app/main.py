import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        raise ValueError("Invalid command")

    cmd, source_path, destination_path = parts

    if cmd != "mv":
        raise ValueError("Command not found")

    destination_dir, new_file_name = os.path.split(destination_path)

    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    os.replace(source_path, os.path.join(destination_dir, new_file_name))
