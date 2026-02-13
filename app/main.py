import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    cmd, src, dst = parts
    if cmd != "mv" or src == dst:
        return
    if not os.path.isfile(src):
        return

    if dst.endswith("/") or dst.endswith(os.sep):
        final_dst = os.path.join(dst, os.path.basename(src))
    else:
        final_dst = dst

    dir_path = os.path.dirname(final_dst)
    if dir_path:
        dir_path = os.path.normpath(dir_path)
        current = ""

        for part in dir_path.replace("\\", "/").split("/"):
            if not part:
                continue
            current = os.path.join(current, part) if current else part
            if not os.path.exists(current):
                os.mkdir(current)

    with open(src, "rb") as fsrc, open(final_dst, "wb") as fdst:
        fdst.write(fsrc.read())

    os.remove(src)
