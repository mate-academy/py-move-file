import os


def move_file(command: str) -> None:
    todo, file_from, file_to, *_ = command.split() + [None] * 2
    if todo != "mv" or any([file_from, file_to]) is None:
        print("Usage: mv SOURCE DEST")
        return

    if not os.path.exists(file_from):
        print("File not found:", file_from)
        return

    if file_to.endswith("/"):
        file_to = os.path.join(file_to, os.path.basename(file_from))

    dir_path_to = os.path.dirname(os.path.abspath(file_to))
    dir_path_from = os.path.dirname(os.path.abspath(file_from))

    if not os.path.exists(dir_path_to):
        os.mkdir(dir_path_to)

    if dir_path_from == dir_path_to:
        os.rename(file_from, file_to)
        return

    with open(file_from, "r") as fs_file_from:
        with open(file_to, "w") as fs_file_to:
            fs_file_to.write(fs_file_from.read())
            os.remove(file_from)
