import os


def move_file(command: str) -> None:
    parts = command.split(" ")

    if parts[0] != "mv" or len(parts) != 3 or parts[1] == parts[2]:
        return

    src = parts[1]
    dest = parts[2]

    if not os.path.exists(src):
        return

    dir_path = os.path.dirname(dest)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    with open(src, "r") as f_src, open(dest, "w") as f_dest:
        f_dest.write(f_src.read())

    os.remove(src)
