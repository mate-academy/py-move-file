import os


def move_file(command: str) -> None:
    command, target_file, destination = command.split()
    destination_path = os.path.dirname(destination)
    if command != "mv":
        raise ValueError("Command not found.")
    if not os.path.exists(target_file):
        raise FileNotFoundError("Target file not found.")
    if destination.endswith("/"):
        raise ValueError("Name of destination file is not found")

    if destination_path:
        os.makedirs(destination_path, exist_ok=True)

    os.replace(target_file, destination)
