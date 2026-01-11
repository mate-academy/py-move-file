import os


def move_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "mv":
        return  # invalid command

    src, dst = parts[1], parts[2]

    if dst.endswith("/"):
        dst = os.path.join(dst, os.path.basename(src))

    dst_dir = os.path.dirname(dst)
    if dst_dir and not os.path.exists(dst_dir):
        os.makedirs(dst_dir, exist_ok=True)

    with open(src, "r") as f_src:
        content = f_src.read()
    with open(dst, "w") as f_dst:
        f_dst.write(content)

    os.remove(src)
