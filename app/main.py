import os
import shutil
from pathlib import Path


def move_file(command: str) -> None:
    try:
        parts = command.split()
        if not (len(parts) == 3 and parts[0] == "mv"):
            return
        _, source_file, full_path = parts
        if source_file == full_path:
            return
        if full_path.endswith("/"):
            full_path = os.path.join(full_path, source_file)
        file_path = os.path.dirname(full_path)
        if file_path:
            current_path = ""
            for directory in Path(file_path).parts:
                current_path = os.path.join(current_path, directory)
                if not os.path.exists(current_path):
                    os.mkdir(current_path)
        shutil.copy2(source_file, full_path)
        os.remove(source_file)
    except FileNotFoundError:
        pass
