import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source_file, destination_path = parts

    if source_file == destination_path:
        return

    if (destination_path.endswith(os.path.sep)
            or destination_path.endswith("/")):
        destination_path = os.path.join(destination_path, source_file)

    directory = os.path.dirname(destination_path)

    if directory:
        normalized_dir = os.path.normpath(directory)
        path_parts = normalized_dir.split(os.path.sep)
        current_path = ""

        for part in path_parts:
            if not part:
                continue
            current_path = os.path.join(current_path, part)
            if not os.path.exists(current_path):
                os.mkdir(current_path)

    with open(source_file, "r") as file_in:
        content = file_in.read()

    with open(destination_path, "w") as file_out:
        file_out.write(content)

    os.remove(source_file)
