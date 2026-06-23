import os


def move_file(command_str: str) -> None:
    parts = command_str.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format.")

    src = parts[1]
    dest = parts[2]

    if src == dest:
        return

    if dest.endswith("/"):
        dest_dir = dest
        file_name = os.path.basename(src)
        final_dest = os.path.join(dest_dir, file_name)
    else:
        dest_dir = os.path.dirname(dest)
        final_dest = dest

    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    os.replace(src, final_dest)
