import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format."
                         " Expected format: 'mv source destination'")

    source_path = parts[1]
    destination_path = parts[2]

    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file {source_path} does not exist")

    if destination_path.endswith("/"):
        os.makedirs(destination_path, exist_ok=True)
        destination_path = os.path.join(destination_path,
                                        os.path.basename(source_path))
    else:
        destination_dir = os.path.dirname(destination_path)
        if destination_dir and not os.path.exists(destination_dir):
            os.makedirs(destination_dir, exist_ok=True)

    os.rename(source_path, destination_path)
