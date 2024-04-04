import os


def move_file(command: str) -> None:
    if not command.startswith("mv "):
        return
    _, source_file, destination = command.split()
    destination = destination.rstrip("/")

    if not os.path.exists(source_file):
        return

    destination_dir, new_file = os.path.split(destination)

    if not new_file:
        new_file = os.path.basename(source_file)

    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    destination_path = os.path.join(destination_dir, new_file)

    if os.path.exists(destination_path):
        return

    os.rename(source_file, destination_path)
