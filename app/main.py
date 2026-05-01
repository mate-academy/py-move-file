import os


def move_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    _, src, dst = parts

    if src == dst:
        return

    if not os.path.exists(src):
        raise FileNotFoundError(f"No such file: '{src}'")

    def make_dirs(path: str) -> None:
        """Create nested directories step by step."""
        path = path.replace("\\", "/")
        parts = path.split("/")
        current = ""

        for part in parts:
            if not part:
                continue
            current = part if current == "" else os.path.join(current, part)
            if not os.path.exists(current):
                os.mkdir(current)

    # Determine destination path
    if dst.endswith("/"):
        # Destination is a directory
        dir_path = dst.rstrip("/")
        file_name = os.path.basename(src)
        final_path = os.path.join(dir_path, file_name)

    elif "/" in dst:
        # Destination includes directories + file name
        dir_path, file_name = os.path.split(dst)
        make_dirs(dir_path)
        final_path = dst

    else:
        # Simple rename in current directory
        final_path = dst

    # Ensure target directory exists
    target_dir = os.path.dirname(final_path)
    if target_dir:
        make_dirs(target_dir)

    # Copy file content
    with open(src, "rb") as f_in, open(final_path, "wb") as f_out:
        f_out.write(f_in.read())

    # Remove source file
    os.remove(src)
