import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return
    _, file1, file2 = parts
    if file1 == file2:
        return
    try:
        directory_path = os.path.dirname(file2)
        if directory_path:
            os.makedirs(directory_path, exist_ok=True)
        os.replace(file1, file2)

    except FileNotFoundError:
        return
