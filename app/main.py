import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or "mv" not in command:
        raise ValueError(
            "Error: Invalid command format."
        )

    mv, source_path, destination_path = parts

    if destination_path.endswith("/"):
        destination_path = os.path.join(
            destination_path, os.path.basename(source_path)
        )

    destination_dir = os.path.dirname(destination_path)

    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    os.rename(source_path, destination_path)
