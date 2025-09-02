import os


def move_file(command: str) -> None:
    split_command = command.split()
    cmd, src, dst = split_command
    if cmd != "mv" or src == dst:
        raise ValueError("Invalid move command")

    dest_dir = os.path.dirname(dst)
    if dest_dir and not os.path.isdir(dest_dir):
        parts = dest_dir.split('/')
        current = ''
        for part in parts:
            current = os.path.join(current, part) if current else part
            if not os.path.isdir(current):
                os.mkdir(current)

    with open(src, 'r') as f:
        content = f.read()
    with open(dst, 'w') as f:
        f.write(content)
    os.remove(src)
