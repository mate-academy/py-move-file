import os


def move_file(command: str) -> None:
    comm, source, dest = command.split()

    if comm != "mv" or not os.path.isfile(source):
        return

    if dest.endswith("/") or os.path.isdir(dest):
        destination = os.path.join(dest, os.path.basename(source))
    else:
        destination = dest

    os.makedirs(os.path.dirname(destination) or ".", exist_ok=True)

    with open(source, "rb") as src, open(destination, "wb") as dst:
        dst.write(src.read())

    os.remove(source)
