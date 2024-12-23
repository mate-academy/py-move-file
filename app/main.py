import os


def move_file(command: str) -> None:
    parts = command.split()
    file, new_file = parts[1], parts[2]
    if not os.path.isfile(file):
        raise FileNotFoundError(f"No such file: '{file}'")
    if new_file.endswith("/"):
        os.makedirs(new_file, exist_ok=True)
        new_file = os.path.join(new_file, os.path.basename(file))
    else:
        parent_dir = os.path.dirname(new_file)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)
    if os.path.isfile(new_file):
        raise FileExistsError(
            f"Cannot move '{file}' to '{new_file}': file already exists."
        )
    os.rename(file, new_file)
    print(f"Moved '{file}' to '{new_file}'")
