import os


def move_file(command: str) -> None:
    parts = command.split(" ", 2)
    if len(parts) != 3 or parts[0] != "mv":
        return
    _, src, dst = parts

    # 1. Validate source
    if not os.path.exists(src) or not os.path.isfile(src):
        raise FileNotFoundError(f"Source file not found or not a file: '{src}'")

    # 2. Compute final path and target directory
    if dst.endswith(os.sep):
        dest_dir = dst.rstrip(os.sep)
        filename = os.path.basename(src)
        final_path = os.path.join(dest_dir, filename)
    else:
        final_path = dst
        dest_dir = os.path.dirname(final_path)

    # 3. Create parent directories step by step
    if dest_dir:
        # Normalize separators so we split correctly on this OS
        dest_dir = os.path.normpath(dest_dir)
        is_abs = os.path.isabs(dest_dir)

        parts = dest_dir.split(os.sep)
        # Start from root if absolute, otherwise from current working dir
        curr = os.sep if is_abs else os.getcwd()
        if is_abs:
            parts = parts[1:]  # first element is empty for absolute paths

        for part in parts:
            curr = os.path.join(curr, part)
            if not os.path.exists(curr):
                os.mkdir(curr)

    # 4. Copy file in binary mode
    with open(src, "rb") as f_src, open(final_path, "wb") as f_dst:
        f_dst.write(f_src.read())

    # 5. Remove original
    os.remove(src)
