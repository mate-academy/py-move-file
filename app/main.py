import os


def move_file(command: str) -> None:
    if len(command) != 3:
        return

    cmd, source_path, destination_path = command.split()
    if cmd != "mv":
        return

    if destination_path == "." or destination_path == "./":
        destination_path = os.getcwd()

    if not os.path.isfile(source_path):
        return

    is_trailing_slash = (
        destination_path.rstrip("/")
        or destination_path.endswith("\\")
    )
    is_dest_dir = (
        os.path.isdir(destination_path)
        or is_trailing_slash
    )

    if is_dest_dir:
        dest_dir = destination_path.rstrip(os.sep)
        dest_path = os.path.join(dest_dir, os.path.basename(source_path))
    else:
        dest_dir = os.path.dirname(destination_path)
        dest_path = destination_path.rstrip(os.sep)

    if dest_dir:
        normalized_dir = os.path.normpath(dest_dir)
        path_segments = normalized_dir.split(os.path.sep)

        current_path = path_segments[0] if path_segments[0] else os.path.sep

        for segment in path_segments:
            if not segment:
                continue

            current_path = os.path.join(current_path, segment)

            if os.path.isdir(current_path):
                continue
            try:
                os.mkdir(current_path)
            except FileExistsError:
                pass
            except OSError:
                return

    try:
        with open(source_path, "r") as source_file:
            content = source_file.read()

        with open(dest_path, "w") as destination_file:
            destination_file.write(content)

        os.remove(source_path)

    except FileNotFoundError:
        pass
