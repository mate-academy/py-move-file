import os


def move_file(command: str) -> None:
    action, file, destination = command.split()
    destination_parts = destination.split("/")
    if destination_parts[-1] == "":
        destination_is_dir = True
        destination_parts = destination_parts[:-1]
    else:
        destination_is_dir = False
    destination_dir = "/".join(destination_parts[:-1])
    destination_file = destination_parts[-1]
    if destination_dir != "":
        os.makedirs(destination_dir, exist_ok=True)
    destination_path = os.path.join(destination_dir, destination_file)
    if os.path.exists(destination_path):
        os.remove(destination_path)
    os.rename(file, destination_path)
    if destination_is_dir:
        os.remove(destination_path)
