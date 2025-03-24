import os


def move_file(command: str) -> None:
    command_data = command.split()
    source = command_data[1]
    destination = command_data[2]

    if not os.path.exists(source):
        raise FileNotFoundError(f"Source file {source} not found")

    dest_parts = destination.split("/")

    if destination.endswith("/"):
        dir_path = destination.rstrip("/")
        file_name = os.path.basename(source)
    else:
        file_name = dest_parts[-1]
        dir_parts = dest_parts[:-1] if len(dest_parts) > 1 else []

    if dir_parts:
        dir_path = os.path.join(*dir_parts)
        os.makedirs(dir_path, exist_ok=True)
        full_destination = os.path.join(dir_path, file_name)
    else:
        full_destination = file_name

    os.rename(source, full_destination)
