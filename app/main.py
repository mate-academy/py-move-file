import os


def move_file(command: str) -> None:
    com_ch = command.split()
    if len(com_ch) != 3:
        return
    else:
        comm, source, dest = com_ch[0], com_ch[1], com_ch[2]

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
