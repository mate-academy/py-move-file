import os


def move_file(command: str) -> None:
    tokens = command.split(" ")
    if len(tokens) != 3 or tokens[0] != "mv":
        return

    _, source, dest = tokens

    if dest.endswith("/"):
        dest_dir = dest[:-1]
        final_filename = os.path.basename(source)
        path = (dest_dir + "/" + final_filename).split("/")
        is_file = True
    else:
        path = dest.split("/")
        is_file = "." in path[-1]

    dir_parts = path[:-1] if is_file else path
    current = ""
    for part in dir_parts:
        current = os.path.join(current, part)
        try:
            os.mkdir(current)
        except FileExistsError:
            pass

    final_path = os.path.join(*path)

    with open(source, "r") as old_file, open(final_path, "w") as new_file:
        new_file.write(old_file.read())

    os.remove(source)
