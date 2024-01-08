import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        raise ValueError(
            "Error: Invalid command format. "
            "Use 'mv source_path destination_path'."
        )

    source_path, destination_path = parts[1], parts[2]

    if not os.path.exists(source_path):
        raise ValueError(
            f"Error: Source file '{source_path}' not found."
        )

    if not destination_path:
        raise ValueError(
            "Error: Destination path is empty."
        )

    is_directory = destination_path.endswith("/")

    if is_directory:
        destination_path = os.path.join(
            destination_path, os.path.basename(source_path)
        )

    destination_dir = os.path.dirname(destination_path)
    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir, exist_ok=True)

    try:
        with open(source_path, "rb") as source_file:
            with open(destination_path, "wb") as destination_file:
                destination_file.write(source_file.read())
        print(f"File '{source_path}' moved to"
              f" '{destination_path}' successfully.")
        os.remove(source_path)
    except Exception as e:
        print(f"Error: {e}")
