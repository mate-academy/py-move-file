import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format")
    cmd, source_file, destination_file = parts

    if destination_file.endswith(os.sep):
        destination_file = os.path.join(destination_file,
                                        os.path.basename(source_file))

    dest_dir = os.path.dirname(destination_file)
    if dest_dir:
        dest_dir = os.path.normpath(dest_dir)
        parts = dest_dir.split(os.sep)
        path_accumulate = os.getcwd()  # стартуємо з поточної папки
        for part in parts:
            path_accumulate = os.path.join(path_accumulate, part)
            if not os.path.exists(path_accumulate):
                os.mkdir(path_accumulate)
    try:
        with (open(source_file, "rb") as src,
              open(destination_file, "wb") as dst):
            dst.write(src.read())

        os.remove(source_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Source file {source_file} does not exist")
