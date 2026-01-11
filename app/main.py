import os
import shutil


def move_file(command: str) -> None:
    frag_com = command.split()
    if len(frag_com) != 3 or frag_com[0] != "mv":
        return
    source_file = frag_com[1]
    way = frag_com[2]
    if not os.path.exists(source_file):
        return
    if way.endswith("/"):
        way = os.path.join(way, os.path.basename(source_file))
    dest_dirs = os.path.dirname(way)
    if dest_dirs and not os.path.exists(dest_dirs):
        os.makedirs(dest_dirs, exist_ok=True)
    shutil.move(source_file, way)
