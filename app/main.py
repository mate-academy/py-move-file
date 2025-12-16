import os


def move_file(command: str) -> None:
    try:
        command, file_src, dst = command.split()
    except ValueError:
        return

    if command != "mv" or file_src == dst:
        return

    if not os.path.isfile(file_src):
        return

    *dirs, _ = dst.split("/")
    if dirs:
        os.makedirs(os.path.join(*dirs), exist_ok=True)
    with open(file_src) as f_src:
        with open(dst, "w") as f_dst:
            f_dst.write(f_src.read())

    os.remove(file_src)
