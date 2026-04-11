import os
import shlex
import shutil


def move_file(command: str) -> None:
    try:
        tokens = shlex.split(command)
    except ValueError as e:
        raise ValueError(f"Shell parsing error: {e}")
    if len(tokens) != 3 or tokens[0] != "mv":
        raise ValueError("Invalid command format. Use: mv <src> <dest>")
    # Expand ~ and get absolute paths for safety
    src = os.path.abspath(os.path.expanduser(tokens[1]))
    dest_raw = os.path.expanduser(tokens[2])
    if not os.path.exists(src):
        raise FileNotFoundError(f"Source not found: {src}")
    if os.path.isdir(src):
        raise IsADirectoryError("This function only handles files.")
    # Determine final destination path
    if dest_raw.endswith((os.path.sep, "/")) or os.path.isdir(dest_raw):
        dest = os.path.join(dest_raw, os.path.basename(src))
    else:
        dest = dest_raw
    dest = os.path.abspath(dest)
    if src == dest:
        return
    # Ensure parent directory exists
    dir_path = os.path.dirname(dest)
    if dir_path:
        create_parent_dirs_stepwise(dir_path)
    try:
        shutil.copy2(src, dest)
        os.remove(src)
    except Exception:
        if os.path.exists(dest):
            try:
                os.remove(dest)
            except Exception:
                pass
        raise


def create_parent_dirs_stepwise(path: str) -> None:
    if not path:
        return
    path = os.path.abspath(path)
    drive, tail = os.path.splitdrive(path)
    parts = tail.strip(os.path.sep).split(os.path.sep)
    cur = drive + os.path.sep if drive else \
        (os.path.sep if path.startswith(os.path.sep) else "")
    for part in parts:
        cur = os.path.join(cur, part) if cur else part
        if os.path.exists(cur):
            if not os.path.isdir(cur):
                raise FileExistsError(f"Path exists and is "
                                      f"not a directory: {cur}")
            continue
        try:
            os.mkdir(cur)
        except FileExistsError:
            if not os.path.isdir(cur):
                raise
