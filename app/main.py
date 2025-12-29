import os


def move_file(command: str) -> None:
    parts = command.split()
    command_name, source_path, destination_path = parts
    if command_name != "mv" or len(parts[1:]) != 2:
        raise ValueError(f"{command_name} is not a valid command")
    if not os.path.exists(source_path) or not os.path.isfile(source_path):
        raise FileNotFoundError(f"Source path {source_path} does not exist")
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
