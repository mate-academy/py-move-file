import os


def move_file(command: str) -> None:

    parts = command.split(maxsplit=2)
    if len(parts) != 3:
        raise ValueError("Invalid command format")

    cmd, src, dest = parts

    if cmd != "mv":
        raise ValueError("Only mv command is supported")

    if not os.path.isfile(src):
        raise FileNotFoundError(src)

    if dest.endswith(os.path.sep):
        os.makedirs(dest, exist_ok=True)
        final_path = os.path.join(dest, os.path.basename(src))
    else:
        dir_name = os.path.dirname(dest)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        final_path = dest

    with open(src, "rb") as source, open(final_path, "wb") as target:
        target.write(source.read())

    os.remove(src)
