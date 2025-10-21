import os


def move_file(command: str) -> None:
    try:
        command_name, source_path, destination_path = command.split()
    except ValueError:
        return

    if command_name != "mv":
        return

    if not os.path.isfile(source_path):
        return

    destination_path = os.path.normpath(destination_path)
    source_path = os.path.normpath(source_path)

    if destination_path.endswith(os.path.sep) or os.path.isdir(destination_path):
        file_name = os.path.basename(source_path)
        full_destination_path = os.path.join(destination_path, file_name)
    else:
        full_destination_path = destination_path

    if os.path.abspath(source_path) == os.path.abspath(full_destination_path):
        return

    dest_dir = os.path.dirname(full_destination_path)
    if dest_dir:
        norm_dir = os.path.normpath(dest_dir)
        parts = norm_dir.split(os.sep)

        current_path = parts[0] if os.path.isabs(norm_dir) else ""
        for part in parts[1:] if os.path.isabs(norm_dir) else parts:
            current_path = os.path.join(current_path, part)
            if not os.path.exists(current_path):
                os.mkdir(current_path)

    try:
        with open(source_path, "r") as file_in, open(full_destination_path, "w") as file_out:
            content = file_in.read()
            file_out.write(content)
        os.remove(source_path)
    except FileNotFoundError:
        pass
