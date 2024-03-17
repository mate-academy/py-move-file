import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[0] == "mv":
        source_path = parts[1]
        destination_path = parts[2]
        if "/" in destination_path:
            dir_path = os.path.dirname(destination_path)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path, exist_ok=True)

        os.rename(source_path, destination_path)
