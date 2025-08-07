import os


def move_file(command: str) -> None:
    # Expected command format: "mv source destination"
    parts = command.split(maxsplit=2)
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format")

    _, src, dest = parts

    # If destination ends with
    if dest.endswith("/"):
        dest = os.path.join(dest, os.path.basename(src))

    # Check if source and destination refer to the same absolute path
    if os.path.abspath(src) == os.path.abspath(dest):
        # Same file, do nothing to avoid data loss
        return

    dest_dir = os.path.dirname(dest)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir, exist_ok=True)

    # Copy file content and remove source file
    with open(src, "rb") as fsrc:
        content = fsrc.read()

    with open(dest, "wb") as fdest:
        fdest.write(content)

    os.remove(src)
