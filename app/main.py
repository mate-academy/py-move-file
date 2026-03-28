import os


def move_file(command: str) -> None:
    if command == "":
        return

    parts = command.split(" ")
    if len(parts) != 3 or parts[0] != "mv":
        return

    cmd, source_path, destination_path = parts

    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file '{source_path}' does not exist.")

    if os.path.isdir(source_path):
        return

    if destination_path.endswith("/"):
        source_filename = os.path.basename(source_path)
        destination_path = os.path.join(destination_path, source_filename)

    destination_dir = os.path.dirname(destination_path)

    if destination_dir and not os.path.exists(destination_dir):
        path_parts = []
        current_dir = destination_dir

        while current_dir and current_dir != ".":
            path_parts.append(current_dir)
            current_dir = os.path.dirname(current_dir)

        path_parts.reverse()

        for dir_path in path_parts:
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)

    if os.path.abspath(source_path) == os.path.abspath(destination_path):
        return

    with open(source_path, "rb") as src, open(destination_path, "wb") as dst:
        dst.write(src.read())

    os.remove(source_path)
