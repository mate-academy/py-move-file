import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Command must be in the format 'mv source destination'"
        )

    src = parts[1]
    dst = parts[2]

    if not os.path.exists(src):
        raise FileNotFoundError(f"Source file '{src}' not found.")

    if dst.endswith("/"):
        os.makedirs(dst, exist_ok=True)
        dst = os.path.join(dst, os.path.basename(src))
    else:
        dst_dir = os.path.dirname(dst)
        if dst_dir and not os.path.exists(dst_dir):
            os.makedirs(dst_dir, exist_ok=True)

    os.rename(src, dst)
    print(f"File '{src}' was moved to '{dst}'")
