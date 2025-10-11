import os
from typing import List


def move_file(command: str) -> None:
    parts: List[str] = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    src: str = parts[1]
    dest: str = parts[2]

    if not os.path.exists(src):
        return

    if dest.endswith("/"):
        os.makedirs(dest, exist_ok=True)
        dest = os.path.join(dest, os.path.basename(src))
    else:
        dest_dir: str = os.path.dirname(dest)
        if dest_dir:
            os.makedirs(dest_dir, exist_ok=True)

    with open(src, "r", encoding="utf-8") as src_file, open(
        dest, "w", encoding="utf-8"
    ) as dest_file:
        dest_file.write(src_file.read())

    os.remove(src)
