import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        raise ValueError("Invalid command")

    if parts[0] != "mv":
        raise ValueError("Command not found")

    current_file_path = parts[1]
    new_file_path = parts[2]

    destination_dir, new_file_name = os.path.split(new_file_path)

    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    os.replace(current_file_path, os.path.join(destination_dir, new_file_name))
