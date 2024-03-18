import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[0] == "mv":
        source_path, destination_path = parts[1], parts[2]
        dir_path = os.path.dirname(destination_path)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
        if os.path.exists(destination_path):
            os.remove(destination_path)
        os.rename(source_path, destination_path)
