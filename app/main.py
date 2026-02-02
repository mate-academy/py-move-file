import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command")

    _, src, dest = parts

    if dest.endswith(os.sep):
        dest = os.path.join(dest, os.path.basename(src))

    dest_dir = os.path.dirname(dest)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with open(src, "r") as f:
        content = f.read()

    with open(dest, "w") as f:
        f.write(content)

    os.remove(src)
