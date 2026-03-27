import os
import shlex


def move_file(command: str) -> None:
    parts = shlex.split(command)
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Error")
    src, dst = parts[1], parts[2]

    if not os.path.isfile(src):
        raise FileNotFoundError("Error")

    is_dir_hint = dst.endswith("/") or dst.endswith(os.sep)
    if is_dir_hint:
        dest_dir = dst.rstrip("/\\")
        dest_name = os.path.basename(src)
        dest_path = os.path.join(dest_dir,
                                 dest_name) if dest_dir else dest_name
    else:
        dest_dir, dest_name = os.path.split(dst)
        dest_path = dst

    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with open(src, "rb") as f_in, open(dest_path, "wb") as f_out:
        f_out.write(f_in.read())

    os.remove(src)
