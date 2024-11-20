import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return

    if parts[2].endswith("/"):
        new_path = os.path.join(parts[2], os.path.basename(parts[1]))
    else:
        new_path = parts[2]

    directory = os.path.dirname(new_path)
    if directory and not os.path.exists(directory):
        new_dir = ""
        for part in directory.split("/"):
            new_dir = os.path.join(new_dir, part)
            if not os.path.exists(new_dir):
                os.mkdir(new_dir)

    try:
        os.rename(parts[1], new_path)
    except BaseException:
        raise
