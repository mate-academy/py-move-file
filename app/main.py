import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command")
    _, src, dst = parts
    original_dst = dst
    dst_is_dir = (
        original_dst.endswith(os.path.sep)
        or original_dst.endswith("/")
        or original_dst.endswith("\\")
    )
    src = os.path.normpath(src)
    dst = os.path.normpath(dst)
    if dst_is_dir:
        dst = os.path.join(dst, os.path.basename(src))
    elif os.path.isdir(dst):
        dst = os.path.join(dst, os.path.basename(src))
    dirpath = os.path.dirname(dst)
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)
    with open(src, "rb") as fsrc:
        data = fsrc.read()
    with open(dst, "wb") as fdst:
        fdst.write(data)
    os.remove(src)
