import os
from os import mkdir


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return

    if parts[0] != "mv":
        return

    _, src, way = parts

    if not os.path.exists(src):
        return

    if way.endswith("/"):
        way = os.path.join(way, os.path.basename(src))

    dir_path = os.path.dirname(way)
    if dir_path:
        current = ""
        for i in dir_path.split("/"):
            current = os.path.join(current, i)
            if not os.path.exists(current):
                mkdir(current)

    with open(src, "r") as f, open(way, "w") as g:
        g.write(f.read())

    os.remove(src)
