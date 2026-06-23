import os


def move_file(command_str: str) -> None:
    parts = command_str.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. Expected: "
                         "'mv source destination'")

    src = parts[1]
    dest = parts[2]

    if src == dest:
        return

    if dest.endswith("/") or os.path.isdir(dest):
        dest_dir = dest
        file_name = os.path.basename(src)
        final_dest = os.path.join(dest_dir, file_name)
    else:
        dest_dir = os.path.dirname(dest)
        final_dest = dest

    if dest_dir:
        normalized_path = os.path.normpath(dest_dir)
        path_parts = normalized_path.split(os.sep)

        current_path = ""
        for part in path_parts:
            if not part:
                continue

            current_path = os.path.join(current_path, part) \
                if current_path else part

            try:
                os.mkdir(current_path)
            except FileExistsError:
                if os.path.isdir(current_path):
                    pass
                else:
                    raise

    os.replace(src, final_dest)
