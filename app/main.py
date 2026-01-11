import os
import shutil


def move_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Invalid command format. Use: mv source_path destination_path"
        )

    src = parts[1]
    dst = parts[2]

    # If destination ends with "/", treat it as a directory
    if dst.endswith("/"):
        os.makedirs(dst, exist_ok=True)
        dst = os.path.join(dst, os.path.basename(src))
    else:
        dst_dir = os.path.dirname(dst)
        if dst_dir:
            os.makedirs(dst_dir, exist_ok=True)

    shutil.copyfile(src, dst)
    os.remove(src)
