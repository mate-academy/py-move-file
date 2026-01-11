import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[0] == "mv":
        src_file = parts[1]
        dest_path = parts[2]
        if dest_path.endswith("/"):
            os.makedirs(dest_path, exist_ok=True)
            dest_file = os.path.join(dest_path, os.path.basename(src_file))
        else:
            dest_dir = os.path.dirname(dest_path)
            if dest_dir != "":
                os.makedirs(dest_dir, exist_ok=True)
            dest_file = dest_path
        shutil.move(src_file, dest_file)
        os.remove(src_file)
