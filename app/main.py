import os.path


def move_file(command: str) -> None:
    (cmd, source_file, dest_full_path) = command.split()
    if (cmd != "mv" or not source_file or not dest_full_path):
        return
    dirs = os.path.dirname(dest_full_path)
    if dirs:
        os.makedirs(dirs, exist_ok=True)
    os.replace(source_file, dest_full_path)
