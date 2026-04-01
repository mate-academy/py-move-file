import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            f"'Invalid command format. Usage: mv {parts[1]} {parts[2]}'"
        )

    source_path = parts[1]
    destination_path = parts[2]

    destination_path_dirs = os.path.dirname(destination_path)

    if destination_path_dirs:
        os.makedirs(destination_path_dirs, exist_ok=True)

    os.rename(source_path, destination_path)
