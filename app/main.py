import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    src, dest = parts[1:]
    if src == dest:
        return

    if not os.path.exists(src) or not os.path.isfile(src):
        return

    if dest.endswith("/") or os.path.isdir(dest):
        dest = os.path.join(dest, os.path.basename(src))

    dir_path = os.path.dirname(dest)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)

    with open(src, "rb") as file_source:
        data = file_source.read()
        with open(dest, "wb") as file_target:
            file_target.write(data)
    os.remove(src)
