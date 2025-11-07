import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, src, dst = parts

    if src == dst:
        return

    if dst.endswith("/"):
        dst = os.path.join(dst, os.path.basename(src))

    dir_path = os.path.dirname(dst)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)

    with open(src, "r") as file_in, open(dst, "w") as file_out:
        content = file_in.read()
        file_out.write(content)

    os.remove(src)
