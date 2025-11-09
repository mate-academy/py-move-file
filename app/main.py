import os


def move_file(command: str) -> None:
    cmd = command.split()
    if len(cmd) != 3:
        return
    cmd_name, source_file_name, destination_path = cmd
    if cmd_name != "mv":
        return

    abs_source_file_name = os.path.realpath(source_file_name)
    abs_destination_path = os.path.realpath(destination_path)

    if abs_source_file_name == abs_destination_path:
        return

    if destination_path.endswith(os.path.sep):
        if not os.path.isdir(abs_destination_path):
            try:
                os.makedirs(abs_destination_path, exist_ok=True)
            except PermissionError:
                raise

        new_destination_path = os.path.join(abs_destination_path,
                                            os.path.basename(source_file_name))
    else:
        dest_dir = os.path.dirname(abs_destination_path)
        if not os.path.isdir(dest_dir):
            try:
                os.makedirs(dest_dir, exist_ok=True)
            except PermissionError:
                raise
        new_destination_path = abs_destination_path

    try:
        with open(abs_source_file_name) as source_file:
            with open(new_destination_path, "w") as destination_file:
                destination_file.write(source_file.read())
    except FileNotFoundError:
        raise
    else:
        try:
            os.remove(abs_source_file_name)
        except PermissionError:
            raise
