import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        raise ValueError("Invalid format")
    source_path = parts[1]
    destination_path = parts[2]
    if not os.path.isdir(destination_path):
        raise FileNotFoundError(f"Source file {destination_path} not found")
    if destination_path.endswith("/"):
        os.makedirs(destination_path, exist_ok=True)
        dst_file = os.path.join(
            destination_path, os.path.basename(source_path)
        )
    else:
        dst_file = destination_path
    os.rename(source_path, dst_file)
