import os


def move_file(mv: str) -> None:
    parts = mv.split()
    source = parts[1]
    dest = parts[2]

    with open(source, "r") as f:
        content = f.read()

    if dest.endswith("/"):
        dest = dest + os.path.basename(source)

    dir_path = os.path.dirname(dest)

    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)

    with open(dest, "w") as new_file:
        new_file.write(content)

    os.remove(source)
