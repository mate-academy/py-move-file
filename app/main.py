import os


def move_file(command_string: str) -> None:
    command, old_file_path, new_file_path, *_ = command_string.split()
    new_file_path = os.path.join(new_file_path)
    old_file_path = os.path.join(old_file_path)

    if command == "mv" and old_file_path != new_file_path:
        new_file_dir = os.path.dirname(new_file_path)
        new_filename = os.path.basename(new_file_path)

        if new_filename:
            if new_file_dir and not os.path.isdir(new_file_dir):
                os.makedirs(new_file_dir, exist_ok=True)
            os.rename(old_file_path, new_file_path)
