import os


def move_file(command: str) -> None:
    parts = command.strip().split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format.")

    src = parts[1]
    dst = parts[2]

    if not os.path.isfile(src):
        raise FileNotFoundError(f"Source file '{src}' not found.")

    if dst.endswith("/"):
        os.makedirs(dst, exist_ok=True)
        dst = os.path.join(dst, os.path.basename(src))
    else:
        dst_dir = os.path.dirname(dst)
        if dst_dir:
            os.makedirs(dst_dir, exist_ok=True)

    with open(src, "rb") as fsrc:
        content = fsrc.read()
    with open(dst, "wb") as fdst:
        fdst.write(content)

    os.remove(src)
