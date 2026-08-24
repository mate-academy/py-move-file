import os
import shutil

def move_file(command: str) -> None:
    parts = command.split()
    source: str = parts[1]
    destination: str = parts[2]
    if destination.endswith('/'):
        destination = os.path.join(destination, os.path.basename(source))
    dest_dir = os.path.dirname(destination)
    if dest_dir and not os.path.exists(dest_dir):
        path_parts = dest_dir.split("/")
        current_path = ""
        for part in path_parts:
            current_path = os.path.join(current_path, part)
            if not os.path.exists(current_path):
                os.mkdir(current_path)
    shutil.copy2(source, destination)
    os.remove(source)
