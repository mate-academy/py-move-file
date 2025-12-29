import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        raise ValueError("Command must contain exactly 3 elements")
    if parts[0] != "mv":
        raise ValueError(f"{parts[0]} is not a valid command")
    command_name, source_path, destination_path = parts
    if not os.path.isfile(source_path):
        raise FileNotFoundError("Source file not found")
    if destination_path[-1] == "/":
        destination_path = os.path.join(
            destination_path, os.path.basename(source_path)
        )
    dir_path = os.path.dirname(destination_path)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
    with open(source_path, "r") as source_file_path:
        content = source_file_path.read()
    with open(destination_path, "w") as destination_file_path:
        destination_file_path.write(content)
    os.remove(source_path)
