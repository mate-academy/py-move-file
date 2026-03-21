import os
from os.path import basename, join


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command")

    src = parts[1]
    dst = parts[2]

    if dst.endswith("/"):
        dst_path = join(dst, basename(src))
    else:
        dst_path = dst

    parent = os.path.dirname(dst_path)

    if parent and not os.path.exists(parent):
        os.makedirs(parent, exist_ok=True)

    with open(src, "rb") as f_in:
        content = f_in.read()

    with open(dst_path, "wb") as f_out:
        f_out.write(content)
        os.remove(src)
