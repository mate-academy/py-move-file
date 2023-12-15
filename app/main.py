import os


def move_file(command: str) -> None:

    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(f"Invalid command: {command}")

    source_file, dest_path = parts[1:]

    if not os.path.exists(source_file):
        raise FileNotFoundError(f"Source file not found: {source_file}")

    if dest_path.endswith("/"):
        dest_path = os.path.join(dest_path, os.path.basename(source_file))
    elif not os.path.isabs(dest_path):

        dest_path = os.path.join(os.getcwd(), dest_path)

    if os.path.exists(dest_path):
        raise FileExistsError(f"Destination file already exists: {dest_path}")

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    try:
        os.rename(source_file, dest_path)
    except OSError as e:
        print(f"Error moving file: {e}")
        raise
