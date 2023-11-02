import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) < 3:
        raise ValueError("Invalid command format.")

    source_file = parts[1]
    destination = parts[2]

    if destination.endswith("/"):
        # Consider it as a directory
        destination_dir = destination
        file_name = os.path.basename(source_file)
        destination_path = os.path.join(destination_dir, file_name)
    else:
        destination_path = destination

    # Create directories if they don't exist
    destination_directory = os.path.dirname(destination_path)
    if destination_directory:
        os.makedirs(destination_directory, exist_ok=True)

    # Attempt to move the file
    os.rename(source_file, destination_path)
