import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Invalid command format. Expected: mv source destination"
        )

    src = parts[1]
    dst = parts[2]

    if not os.path.isfile(src):
        raise FileNotFoundError(f"Source file '{src}' does not exist")

    if dst.endswith("/"):
        dst = dst + os.path.basename(src)

    dst_dir = os.path.dirname(dst)
    if dst_dir and not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    with open(src, "r") as f:
        content = f.read()

    with open(dst, "w") as f:
        f.write(content)

    os.remove(src)
