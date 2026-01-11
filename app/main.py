import os


def move_file(command: str) -> None:
    _, src, dest = command.split()

    if dest.endswith("/"):
        os.makedirs(dest, exist_ok=True)
        dest = os.path.join(dest, os.path.basename(src))
    else:
        dest_dir = os.path.dirname(dest)
        if dest_dir:
            os.makedirs(dest_dir, exist_ok=True)

    os.rename(src, dest)
