import os


def move_file(command: str) -> None:
    my_split = command.split()
    if len(my_split) != 3 or my_split[0] != "mv":
        return
    src, dst = my_split[1], my_split[2]
    if dst.endswith("/"):
        os.makedirs(dst, exist_ok=True)
        dst = os.path.join(dst, os.path.basename(src))
    else:
        dir_path = os.path.dirname(dst)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
    os.rename(src, dst)
