import os


def move_file(command: str) -> None:
    parts: list[str] = command.strip().split(" ", maxsplit=2)

    if len(parts) != 3:
        raise ValueError

    cmd, source_path, dest_path = parts

    if cmd != "mv":
        raise ValueError

    if not os.path.isfile(source_path):
        raise FileNotFoundError

    dest_is_dir = dest_path.endswith(os.sep) or os.path.isdir(dest_path)

    if dest_is_dir:
        dest_dir = dest_path.rstrip(os.sep)
        dest_filename = os.path.basename(source_path)
        full_dest_path = os.path.join(dest_dir, dest_filename)
    else:
        dest_dir = os.path.dirname(dest_path)
        dest_filename = os.path.basename(dest_path)
        full_dest_path = dest_path

    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir, exist_ok=True)

    with open(source_path, "r") as src_file:
        content = src_file.read()

    with open(full_dest_path, "w") as dst_file:
        dst_file.write(content)

    os.remove(source_path)
