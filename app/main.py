import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format")

    _, src, dst = parts

    if not os.path.isfile(src):
        raise FileNotFoundError(f"Source file not found: {src}")

    if dst == os.sep:
        dir_path = os.sep
        file_name = os.path.basename(src)

    elif dst.endswith(os.sep):
        dir_path = dst.rstrip(os.sep)
        file_name = os.path.basename(src)
    else:
        dir_path, file_name = os.path.split(dst)

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    new_path = os.path.join(dir_path, file_name) if dir_path else file_name

    with open(src, "rb") as f_in, open(new_path, "wb") as f_out:
        f_out.write(f_in.read())

    os.remove(src)
