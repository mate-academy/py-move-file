import os


def move_file(command: str) -> None:
    """Move a file from one path to another.

    The `command` string should follow the format of the Linux `mv` command.

    Example:
        mv <src> <dst>

    - If the destination path ends with a trailing slash, it is treated as a
      directory.
    - Intermediate directories in the destination path are created as needed.
    """
    parts_command = command.split()

    if len(parts_command) != 3:
        return

    mv, source, destination = parts_command

    if mv != "mv":
        return

    if source == destination:
        return

    try:
        with open(source, "r") as src_file:
            content = src_file.read()

    except FileNotFoundError:
        return

    if destination.endswith(os.path.sep) or destination.endswith("/"):
        # Treat destination as a directory.
        destination = os.path.join(destination, os.path.basename(source))

    dst_dir = os.path.dirname(destination)
    if dst_dir and not os.path.exists(dst_dir):
        os.makedirs(dst_dir, exist_ok=True)

    with open(destination, "w") as dest_file:
        dest_file.write(content)
    # Move (rename) the file.
    os.remove(source)
