import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return None

    command_name, source_path, destination_path = parts

    if command_name != "mv":
        return None

    if not os.path.isfile(source_path):
        raise FileNotFoundError

    is_dir_dst = (destination_path.endswith(os.path.sep)
                  or os.path.isdir(destination_path))
    source_filename = os.path.basename(source_path)

    if is_dir_dst:
        destination_dir = destination_path.rstrip("/")
        destination_filename = source_filename
    else:
        destination_dir, destination_filename = os.path.split(destination_path)

    if destination_dir:
        path_so_far = ""
        for dir_part in os.path.normpath(destination_dir).split(os.path.sep):
            path_so_far = os.path.join(path_so_far, dir_part)
            if not os.path.isdir(path_so_far):
                os.mkdir(path_so_far)

    final_path = os.path.join(destination_dir, destination_filename) \
        if destination_dir else destination_filename

    with (open(source_path, "rb") as src_file,
          open(final_path, "wb") as dst_file):
        dst_file.write(src_file.read())

    os.remove(source_path)
