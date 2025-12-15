import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return

    action, source_path, destination_path = parts
    if action != "mv" or source_path == destination_path:
        return

    if destination_path.endswith(os.sep):
        filename = os.path.basename(source_path)
        destination_path = os.path.join(destination_path, filename)

    destination_dir = os.path.dirname(destination_path)
    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)
    try:
        with (open(source_path, "rb") as src,
              open(destination_path, "wb") as dst):
            dst.write(src.read())

    except OSError:
        return
    else:
        os.remove(source_path)
