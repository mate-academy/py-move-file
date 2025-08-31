import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    source, dest = parts[1], parts[2]
    if dest == source or not os.path.isfile(source):
        return

    if dest.endswith(os.sep):
        dest = os.path.join(dest, os.path.basename(source))

    way = os.path.dirname(dest)
    if not os.path.dirname(source) and not way:
        os.rename(source, dest)
    else:
        os.makedirs(way, exist_ok=True)

    with open(source, "r") as orig, open(dest, "w") as copied:
        copied.write(orig.read())

    os.remove(source)
