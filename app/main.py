import os


def make_dirs_for_path(path: str) -> None:
    if not path:
        return
    dir_path = path if path.endswith(os.sep) else os.path.dirname(path)
    if not dir_path:
        return
    parts = [p for p in dir_path.split(os.sep) if p != ""]
    current = os.sep if os.path.isabs(dir_path) else ""
    for part in parts:
        current = os.path.join(current, part)
        if not os.path.exists(current):
            os.mkdir(current)


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    cmd, src, dst = parts
    if cmd != "mv":
        return
    if dst.endswith(os.sep):
        target = os.path.join(dst, os.path.basename(src))
    else:
        target = dst
    make_dirs_for_path(target)
    if not os.path.isfile(src):
        raise FileNotFoundError
    with open(src, "rb") as source, open(target, "wb") as destination:
        chunk_size = 64 * 1024
        while True:
            chunk_s = source.read(chunk_size)
            if not chunk_s:
                break
            destination.write(chunk_s)
    os.remove(src)
