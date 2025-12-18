import os


def move_file(command: str) -> None:
    command = command.split()

    if command[0] != "mv" or len(command) != 3:
        raise ValueError("Invalid command")

    old_file, new_file = command[1], command[2]
    has_trailing_sep = new_file.endswith(os.sep)
    normalized = new_file.rstrip(os.sep)
    parts = normalized.split(os.sep)

    if has_trailing_sep:
        dirs = parts
    else:
        dirs = parts[:-1]

    curr = os.getcwd()
    for dir_ in dirs:
        curr = os.path.join(curr, dir_)
        if not os.path.exists(curr):
            os.mkdir(curr)

    if has_trailing_sep:
        dest = os.path.join(normalized, os.path.basename(old_file))
    else:
        dest = new_file

    with open(old_file, "rb") as src, open(dest, "wb") as dst:
        while True:
            chunk = src.read(4096)
            if not chunk:
                break
            dst.write(chunk)

    os.remove(old_file)
