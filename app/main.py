import os


def move_file(command: str) -> None:
    try:
        parts = command.split()
        if not (len(parts) == 3 and parts[0] == "mv"):
            return
        _, source_file, full_path = parts
        if source_file == full_path:
            return
        file_path = os.path.dirname(full_path)
        if file_path:
            os.makedirs(file_path, exist_ok=True)
        os.rename(source_file, full_path)
    except FileNotFoundError:
        pass
