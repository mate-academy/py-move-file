import os


def move_file(command: str) -> None:
    if not command.strip():
        return

    parts = command.strip().split()

    if len(parts) != 3:
        return

    cmd, source, destination = parts

    if cmd != "mv" or source == destination:
        return

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    directory = os.path.dirname(destination)
    if directory and not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except FileExistsError:
            pass

    try:
        os.rename(source, destination)
    except (FileNotFoundError, FileExistsError):
        return
