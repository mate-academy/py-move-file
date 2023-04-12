import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3:
        return
    action, source_file, destination = command_parts
    destination_dir, destination_file = os.path.split(destination)
    if destination_file == "":
        destination_is_dir = True
    else:
        destination_is_dir = False
    if destination_dir != "":
        os.makedirs(destination_dir, exist_ok=True)
    destination_path = os.path.join(destination_dir, destination_file)
    if os.path.exists(destination_path):
        os.remove(destination_path)
    os.rename(source_file, destination_path)
    if destination_is_dir:
        os.remove(destination_path)
