import os
import shutil


def move_file(command: str) -> None | ValueError | FileExistsError:
    parts = command.split(" ")
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid format. Use: mv <source> <destination>")

    src_path, dest_path = parts[1:]

    if not os.path.isfile(src_path):
        raise FileNotFoundError(f"The file '{src_path}' does not exist.")

    dest_dir, dest_file = get_dir_and_file(dest_path)
    dest_file = dest_file if dest_file else os.path.basename(src_path)

    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    dest_path = os.path.join(dest_dir, dest_file)

    shutil.move(src_path, dest_path)


def get_dir_and_file(path: str) -> tuple[str, str]:
    dirs = os.path.dirname(path)
    file_name = os.path.basename(path)
    return dirs, file_name
