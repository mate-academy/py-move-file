import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("The command is incorrect!")

    _, source, dest = parts

    if not os.path.exists(source):
        raise FileNotFoundError(f"No such file: {source}")

    if dest.endswith(os.sep) or os.path.isdir(dest):
        target = os.path.join(dest, os.path.basename(source))
    else:
        target = dest
    if os.path.abspath(source) == os.path.abspath(target):
        return
    target_dir = os.path.dirname(target)
    if target_dir:
        if os.path.exists(target_dir):
            if not os.path.isdir(target_dir):
                raise FileExistsError(
                    f"Cannot create directory '{target_dir}': File exists"
                )
        else:
            os.makedirs(target_dir)
    if os.path.isfile(target):
        os.remove(target)
    with open(source, "rb") as src, open(target, "wb") as dst:
        while True:
            chunk = src.read(1024 * 1024)
            if not chunk:
                break
            dst.write(chunk)
    os.remove(source)
