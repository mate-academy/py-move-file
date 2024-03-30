import os


def move_file(command: str) -> None:
    _, source_file, destination_path = command.split()
    if "/" in destination_path:
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    with open(source_file, "r") as copied_file, open(destination_path, "w") as destination_directory:
        destination_directory.write(copied_file.read())
    os.remove(source_file)
