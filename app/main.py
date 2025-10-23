import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    src = parts[1]
    dst = parts[2]

    if not os.path.isfile(src):
        return

    if dst.endswith("/"):
        dst = os.path.join(dst, os.path.basename(src))

    dir_path = os.path.dirname(dst)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    with open(src, "r") as source_file:
        content = source_file.read()
    with open(dst, "w") as dest_file:
        dest_file.write(content)

    os.remove(src)
