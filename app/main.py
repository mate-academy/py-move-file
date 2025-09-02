import os


def move_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3:
        raise ValueError("Command must be: mv <src> <dst>")
    cmd, src, dst = parts
    if cmd != "mv" or src == dst:
        raise ValueError("Invalid move command")

    if dst.endswith(os.path.sep):
        dst = os.path.join(dst, os.path.basename(src))

    dest_dir = os.path.dirname(dst)
    if dest_dir and not os.path.isdir(dest_dir):
        current = ""
        for part in dest_dir.split(os.path.sep):
            if not part:
                continue
            current = os.path.join(current, part) if current else part
            if not os.path.isdir(current):
                os.mkdir(current)

    with open(src, "rb") as fsrc:
        content = fsrc.read()
    with open(dst, "wb") as fdst:
        fdst.write(content)
    os.remove(src)
