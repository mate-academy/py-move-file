import os


def move_file(filename: str) -> None:
    parts = filename.split()
    if parts[0] == "mv":
        source_path = parts[1]
        dest_path = parts[2]

        if dest_path.endswith("/"):
            final_dest = os.path.join(dest_path, os.path.basename(source_path))
        else:
            final_dest = dest_path

        os.makedirs(os.path.dirname(final_dest), exist_ok=True)
        os.rename(source_path, final_dest)
