import os


def move_file(command: str) -> None:
    command = command.split()
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

    os.rename(old_file, dest)
