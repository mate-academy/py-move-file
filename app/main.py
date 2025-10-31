import os


def move_file(mv: str) -> None:
    parts = mv.split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, dest = parts

    with open(source, "r") as f:
        content = f.read()

    if dest.endswith(os.sep):
        dest = os.path.join(dest, os.path.basename(source))

    dir_path = os.path.dirname(dest)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)

    with open(dest, "w") as new_file:
        new_file.write(content)

    os.remove(source)
