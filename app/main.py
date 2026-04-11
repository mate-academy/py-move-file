import os
import shlex
import shutil


def move_file(command: str) -> None:
    # Use shlex to handle paths with spaces/quotes correctly
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
        os.makedirs(dir_path, exist_ok=True)
    try:
        os.replace(src, dest)
    except OSError:
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
