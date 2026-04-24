import os


def move_file(command: str) -> None:
    parts = command.split()
    _, src, dst = parts

    dest_dir = os.path.dirname(dst)

    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(src, "rb") as src_file:
        content = src_file.read()

    with open(dst, "wb") as dest_file:
        dest_file.write(content)

    os.remove(src)
