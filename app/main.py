import os


def move_file(command: str) -> None:
    _, src, dest = command.split()

    if dest.endswith("/"):
        os.makedirs(dest, exist_ok=True)
        dest = os.path.join(dest, os.path.basename(src))
    else:
        dir_path = os.path.dirname(dest)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

    with open(src, "rb") as src_file, open(dest, "wb") as dest_file:
        dest_file.write(src_file.read())

    os.remove(src)
