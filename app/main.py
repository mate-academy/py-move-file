import os
import shutil


def move_file(command: str) -> None:
    parts = command.strip().split(maxsplit=2)

    if len(parts) != 3 or parts[0] != "mv":
        print("Invalid command")
        return

    _, src, dst = parts

    if src == dst:
        print("Source and destination are the same. Nothing to do.")
        return

    if not os.path.isfile(src):
        print(f"Source file does not exist: {src}")
        return

    # If destination ends with /, treat it as a directory
    if dst.endswith("/"):
        os.makedirs(dst, exist_ok=True)
        dst = os.path.join(dst, os.path.basename(src))
    else:
        dst_dir = os.path.dirname(dst)
        if dst_dir:
            os.makedirs(dst_dir, exist_ok=True)

    try:
        shutil.move(src, dst)
    except Exception as exc:
        print(f"Error while moving file: {exc}")
