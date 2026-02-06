import os


def move_file(command: str) -> None:
    parts = command.split()
    if not (len(parts) == 3 and parts[0] == "mv"):
        return

    source, destination = parts[1], parts[2]

    if destination.endswith("/"):
        filename = os.path.basename(source)
        destination = os.path.join(destination, filename)

    if not os.path.exists(source):
        raise FileNotFoundError(f"{source} not found")
    if not os.path.isfile(source):
        raise IsADirectoryError(f"{source} is a directory")

    destination = os.path.normpath(destination)

    if os.path.abspath(source) == os.path.abspath(destination):
        raise ValueError("Source and destination are the same")
    if os.path.isdir(destination):
        raise IsADirectoryError(f"{destination} is a directory")

    target_dir = os.path.dirname(destination)
    if target_dir:
        drive, path_rest = os.path.splitdrive(target_dir)
        path_rest = path_rest.lstrip(os.sep)
        dir_parts = [p for p in path_rest.split(os.sep) if p]

        current = drive + os.path.sep if drive else ""

        for part in dir_parts:
            current = os.path.join(current, part) if current else part
            if not os.path.exists(current):
                try:
                    os.mkdir(current)
                except FileExistsError:
                    pass

    with open(source, "rb") as src, open(destination, "wb") as dst:
        while True:
            chunk = src.read(65536)
            if not chunk:
                break
            dst.write(chunk)

    os.remove(source)
