import os

def move_file(command: str) -> None:
    parts = command.split(" ")

    if parts[0] != "mv" or len(parts) != 3 or parts[1] == parts[2]:
        return

    _, src, dest = parts

    if not os.path.isfile(src):
        return

    if dest.endswith("/"):
        os.makedirs(dest, exist_ok=True)
        dest = os.path.join(dest, os.path.basename(src))
    else:
        dir_path = os.path.dirname(dest)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

    with open(src, "r") as f_src, open(dest, "w") as f_dest:
        f_dest.write(f_src.read())

    os.remove(src)
