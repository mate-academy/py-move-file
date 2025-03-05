import os


def move_file(command: str) -> None:
    parts = command.split()

    if parts[0] != "mv" or len(parts) != 3:
        return

    mv, src, dst = parts
    dest_dir = os.path.dirname(dst)

    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with open(src, "r") as file_in, open(dst, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(src)
