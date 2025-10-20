import os


def move_file(command: str) -> None:
    command = command.strip()

    if not command.startswith("mv "):
        return

    args = command[3:].strip().split(" ", 1)

    if len(args) != 2:
        return

    source, destination = args

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    dst_dir = os.path.dirname(destination)
    if dst_dir:
        os.makedirs(dst_dir, exist_ok=True)

    try:
        with open(source, "r") as f_src:
            content = f_src.read()
    except FileNotFoundError:
        return

    with open(destination, "w") as f_dst:
        f_dst.write(content)

    os.remove(source)
