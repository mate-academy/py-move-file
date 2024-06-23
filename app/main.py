import os


def move_file(command: str) -> None:
    cmd, src, dest = command.split()

    if cmd == "mv" and dest.endswith("/"):
        os.makedirs(dest, exist_ok=True)
        dest = os.path.join(dest, os.path.basename(src))
    else:
        dest_dir = os.path.dirname(dest)
        if dest_dir:
            os.makedirs(dest_dir, exist_ok=True)

    with open(src, "r") as file_in:
        content = file_in.read()

    with open(dest, "w") as file_out:
        file_out.write(content)

    os.remove(src)
