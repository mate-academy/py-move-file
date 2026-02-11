import os


def move_file(command: str) -> int:

    args = command.split(" ")
    if len(args) != 3:
        return 1

    cmd, src, dest = args

    if cmd != "mv":
        return 1

    source_path = os.path.abspath(src)
    source_file = os.path.basename(source_path)

    if dest.endswith("\\") or dest.endswith("/"):
        dest += source_file

    dest_path = os.path.abspath(dest)
    parent_dir = os.path.dirname(dest_path)

    os.makedirs(parent_dir, exist_ok=True)

    with open(source_path, "r") as source_file:
        content = source_file.read()

    with open(dest_path, "w") as dest_file:
        dest_file.write(content)

    os.remove(source_path)

    return 0
