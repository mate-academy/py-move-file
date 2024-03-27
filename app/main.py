from pathlib import Path
import os


def move_file(command: str) -> None:
    command = command.split()

    if len(command) != 3 or command[0] != "mv":
        raise ValueError("Wrong command.")
    _, old_file, new_path_and_file = command
    old_file_path = Path(old_file)
    if not old_file_path.is_file():
        raise FileNotFoundError(f"File not found: '{old_file}'")
    new_dir, new_file = os.path.split(new_path_and_file)
    if new_dir:
        os.makedirs(new_dir, exist_ok=True)
    try:
        old_file_path.rename(Path(new_dir, new_file))
    except PermissionError:
        raise PermissionError(f"No permission to access the file: "
                              f"'{old_file}'")
