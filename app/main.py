import os


def move_file(command: str) -> None:
    """Move a file from one path to another.

    The `command` string should follow the format of the Linux `mv` command.

    Example:
        mv <src> <dst>

    - If the destination path ends with a trailing slash, it is treated as a
      directory.
    - Intermediate directories in the destination path are created as needed.
    """

    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Command must be in the form: mv <src> <dst>")

    _, src, dst = parts

    if dst.endswith(os.path.sep) or dst.endswith("/"):
        # Treat destination as a directory.
        dst = os.path.join(dst, os.path.basename(src))

    dst_dir = os.path.dirname(dst)
    if dst_dir and not os.path.exists(dst_dir):
        os.makedirs(dst_dir, exist_ok=True)

    # Move (rename) the file.
    os.replace(src, dst)
