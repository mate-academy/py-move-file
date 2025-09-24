import os


def move_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3:
        raise ValueError("Invalid command. "
                         "Expected format: mv source destination")

    mv_cmd, source_path, destination_path = parts
    if mv_cmd != "mv":
        raise ValueError("Command must start with 'mv'")

    if not os.path.isfile(source_path):
        raise FileNotFoundError(f"Source file does not exist "
                                f"or is not a file: {source_path}")

    if destination_path.endswith(os.sep):
        destination_path = os.path.join(destination_path,
                                        os.path.basename(source_path))

    dest_dir = os.path.dirname(destination_path)
    if dest_dir:
        norm_dest_dir = os.path.normpath(dest_dir)
        parts = norm_dest_dir.split(os.sep)
        current_path = ""

        if os.path.isabs(norm_dest_dir):
            if os.name == "nt":
                current_path = parts[0] + os.sep
                parts = parts[1:]
            else:
                current_path = os.sep

        for part in parts:
            if not part:
                continue
            current_path = os.path.join(current_path, part)
            if not os.path.exists(current_path):
                os.mkdir(current_path)

    with open(source_path, "rb") as src_file:
        content = src_file.read()

    with open(destination_path, "wb") as dest_file:
        dest_file.write(content)

    os.remove(source_path)
