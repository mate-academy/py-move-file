import os


def move_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) == 3:
        commandos, source_file, new_file = parts
        if commandos == "mv" and source_file != new_file:
            path, filename = os.path.split(new_file)
            if path:
                os.makedirs(path, exist_ok=True)
            os.replace(source_file, new_file)
            if os.path.exists(source_file):
                os.remove(source_file)
