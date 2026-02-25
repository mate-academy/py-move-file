import os


def move_file(command: str) -> None:
    lines = command.split()
    if len(lines) != 3:
        raise ValueError
    if lines[0] != "mv":
        raise ValueError
    _, src, dst = lines
    if dst.endswith("/"):
        dst = os.path.join(dst, os.path.basename(src))
    dest_dir = os.path.dirname(dst)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)
    with open(src, "rb") as f_src:
        data = f_src.read()
    with open(dst, "wb") as f_dst:
        f_dst.write(data)
    os.remove(src)
