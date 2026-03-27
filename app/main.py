import os


def move_file(command_line: str) -> None:
    command, source_path, dest_path = command_line.split()

    if dest_path.endswith("/"):
        dest_dir = dest_path.rstrip("/")
        file_name = os.path.basename(source_path)
        dest_full_path = os.path.join(dest_dir, file_name)

        os.makedirs(dest_dir, exist_ok=True)

        with open(source_path, "rb") as src_file:
            src_data = src_file.read()

        with open(dest_full_path, "wb") as dest_file:
            dest_file.write(src_data)

        os.remove(source_path)
    else:
        dest_dir = os.path.dirname(dest_path)
        if dest_dir:
            os.makedirs(dest_dir, exist_ok=True)

        if os.path.exists(dest_path):
            os.remove(dest_path)

        os.rename(source_path, dest_path)
