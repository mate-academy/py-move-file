import os


def move_file(command: str) -> None:
    parts = command.split(" ")

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, dest = parts

    file_name = os.path.basename(source)

    if dest.endswith("/"):
        new_path = os.path.join(dest, file_name)
    else:
        new_path = dest

    dir_path = os.path.dirname(new_path)

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    with open(source, "r") as f:
        with open(new_path, "w") as f2:
            f2.write(f.read())

    os.remove(source)
