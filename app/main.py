import os


def move_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    filename = parts[1]
    way = parts[2]

    if "/" not in way:
        if os.path.exists(way):
            return

        try:
            os.rename(filename, way)
        except (FileNotFoundError, FileExistsError):
            return
        return

    if way.endswith("/"):
        if os.path.exists(way) and os.path.isfile(way):
            return

        try:
            os.makedirs(way, exist_ok=True)
        except (FileNotFoundError, FileExistsError):
            return
        way = os.path.join(way, os.path.basename(filename))

    else:
        dest_dir = os.path.dirname(way)
        if os.path.exists(dest_dir) and os.path.isfile(dest_dir):
            return
        try:
            os.makedirs(dest_dir, exist_ok=True)
        except FileExistsError:
            return

    if os.path.exists(way):
        return

    try:
        os.rename(filename, way)
    except (FileNotFoundError, FileExistsError):
        return
