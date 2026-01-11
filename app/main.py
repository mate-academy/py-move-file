import os


def move_file(command: str) -> None:
    # Parse the command
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    src = parts[1]
    dst = parts[-1]

    # Check if source file exists
    if not os.path.isfile(src):
        raise FileNotFoundError(f"Source file '{src}' not found")

    # Determine the destination path
    if dst.endswith("/"):
        if not os.path.exists(dst):
            os.makedirs(dst)
        dst = os.path.join(dst, os.path.basename(src))
    else:
        dst_dir = os.path.dirname(dst)
        if dst_dir and not os.path.exists(dst_dir):
            os.makedirs(dst_dir)

    # Move the file
    os.rename(src, dst)
