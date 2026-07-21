import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    _, src, dst = parts

    if not os.path.exists(src):
        return

    if dst.endswith("/"):
        dst_file_path = os.path.join(
            dst, os.path.basename(src)
        )
    else:
        dst_file_path = dst

    if src == dst_file_path:
        return

    dir_name = os.path.dirname(dst_file_path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)

    with open(src, "r") as file_in, \
            open(dst_file_path, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(src)
