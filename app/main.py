import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format")
    cmd, source_path, dest_path = parts

    if not os.path.isfile(source_path):
        raise ValueError("Source must be an existing file")

    if dest_path.endswith("/"):
        final_dest = os.path.join(dest_path, os.path.basename(source_path))
    else:
        final_dest = dest_path

    dir_name = os.path.dirname(final_dest)

    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(source_path, "rb") as src:
        with open(final_dest, "wb") as dest:
            dest.write(src.read())
    os.remove(source_path)
