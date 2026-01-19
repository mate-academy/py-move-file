from __future__ import annotations

import os
import shutil


def move_file(command: str) -> None:
    """
    Move a file based on a simplified `mv`-like command.

    Supported format: `mv <source> <destination>`
    - If destination ends with `/`, it is treated as a directory and the source
      basename is used as the destination filename.
    - Intermediate destination directories are created if needed.
    """
    parts = command.split()
    if len(parts) != 3:
        raise ValueError("Unsupported command format. Expected: mv <source> <destination>")

    cmd, source_path, destination_path = parts
    if cmd != "mv":
        raise ValueError("Unsupported command format. Expected: mv <source> <destination>")

    if destination_path.endswith("/"):
        destination_path = os.path.join(destination_path, os.path.basename(source_path))

    destination_dir = os.path.dirname(destination_path)
    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    shutil.copyfile(source_path, destination_path)
    os.remove(source_path)
