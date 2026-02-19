import os
import shutil


def move_file(command: str) -> None:
    """
    Move a file from source to destination, similar to 'mv' command.

    Args:
        command (str): Command in the form "mv source destination".

    Raises:
        ValueError: If command format is invalid.
        FileNotFoundError: If source file does not exist.
    """

    parts: list[str] = command.strip().split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. Use: mv source destination")

    _, src, dst = parts

    if not os.path.isfile(src):
        raise FileNotFoundError(f"Source file '{src}' not found.")

    if dst.endswith("/"):
        dst_dir: str = dst.rstrip("/")
        dst_filename: str = os.path.basename(src)
        dst = os.path.join(dst_dir, dst_filename)
    else:
        dst_dir: str = os.path.dirname(dst)

    if dst_dir:
        os.makedirs(dst_dir, exist_ok=True)

    shutil.copy2(src, dst)
    os.remove(src)
