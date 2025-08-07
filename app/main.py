import os


def move_file(command: str) -> None:
    # Expected command format: "mv source destination"
    parts = command.split(maxsplit=2)
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format")

    src = parts[1]
    dest = parts[2]

    # If destination ends with "/", treat as directory
    if dest.endswith("/"):
        dest = os.path.join(dest, os.path.basename(src))

    dest_dir = os.path.dirname(dest)
    if dest_dir and not os.path.exists(dest_dir):
        # Create all intermediate directories including dest_dir
        os.makedirs(dest_dir, exist_ok=True)

    # Move the file: copy content and remove source file
    with open(src, "rb") as fsrc:
        content = fsrc.read()

    with open(dest, "wb") as fdest:
        fdest.write(content)

    os.remove(src)
