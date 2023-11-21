import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[0] == "mv":
        source_file, destination_path = parts[1], parts[2]

        if destination_path.endswith("/"):
            return

        path = os.path.dirname(destination_path)

        if path:
            os.makedirs(path, exist_ok=True)

        os.rename(source_file, destination_path)
