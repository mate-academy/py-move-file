import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        raise ValueError("Invalid format")
    md, source_path, destination_path = parts
    condition = (
        md not in command or
        source_path == destination_path or
        not os.path.isfile(source_path)
)
if condition:
    raise FileNotFoundError(f"Source file {source_path} not found")

    directories_path, file_name = os.path.split(source_path)
    if len(directories_path):
        os.makedirs(directories_path, exist_ok=True)
    os.rename(source_path, destination_path)
