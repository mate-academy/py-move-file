import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format")

    source_path = parts[1]
    destination_path = parts[2]

    if not os.path.isfile(source_path):
        raise FileNotFoundError(
            f"Source file {source_path} does not exist."
        )

    if destination_path.endswith("/"):
        destination_path = os.path.join(
            destination_path, os.path.basename(source_path)
        )

    destination_dir = os.path.dirname(destination_path)
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    os.rename(source_path, destination_path)
