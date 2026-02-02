import os


def move_file(command: str) -> None:
    _, src, dst = command.split()

    if not os.path.isfile(src):
        raise FileNotFoundError(f"Source file '{src}' does not exist")

    if dst.endswith("/"):
        dst = os.path.join(dst, os.path.basename(src))

    dst_dir = os.path.dirname(dst)
    if dst_dir and not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    with open(src, "r") as f:
        content = f.read()

    with open(dst, "w") as f:
        f.write(content)

    os.remove(src)
