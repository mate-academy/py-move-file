import os


def move_file(command: str) -> None:
    parts = command.split()
    cmd, source_path, destination_path = parts
    current_dir = os.getcwd()
    destination_folder, destination_file = os.path.split(destination_path)
    if destination_folder:
        os.makedirs(destination_folder, exist_ok=True)
        source_path = os.path.join(current_dir, source_path)
        destination_path = os.path.join(current_dir, destination_path)
    os.rename(source_path, destination_path)
