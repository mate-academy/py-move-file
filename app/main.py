import os


def move_file(command: str) -> None:
    tokens = command.strip().split()
    if len(tokens) != 3 or tokens[0] != "mv":
        return

    _, source, destination = tokens

    if not os.path.isfile(source):
        return

    if (destination.endswith(os.path.sep)
            or (os.path.altsep and destination.endswith(os.path.altsep))):
        destination = os.path.join(destination, os.path.basename(source))

    dst_dir = os.path.dirname(destination)
    if dst_dir:
        parts = dst_dir.split(os.path.sep)
        if os.path.altsep:
            parts = [p for part in parts for p in part.split(os.path.altsep)]
        path = ""
        for part in parts:
            if not part:
                continue
            path = os.path.join(path, part) if path else part
            if not os.path.exists(path):
                os.mkdir(path)

    with open(source, "rb") as f_src:
        content = f_src.read()
    with open(destination, "wb") as f_dst:
        f_dst.write(content)

    os.remove(source)
