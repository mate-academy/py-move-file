import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    cmd, src, dst = parts

    if not os.path.isfile(src):
        return

    if os.path.isdir(dst):
        dst = os.path.join(dst, os.path.basename(src))
    elif dst.endswith(os.sep) or dst.endswith("/"):
        dst = os.path.join(dst, os.path.basename(src))

    if os.path.abspath(src) == os.path.abspath(dst):
        return

    dir_path = os.path.abspath(os.path.dirname(dst))
    if dir_path:
        os.path.normpath(dir_path)
        components = dir_path.split(os.sep)
        path_accum = "" if not os.path.isabs(dir_path) else os.sep
        for comp in components:
            if not comp:
                continue
            path_accum = os.path.join(path_accum, comp) if path_accum else comp
            if os.path.exists(path_accum) and not os.path.isdir(path_accum):
                raise FileExistsError(
                    f"Cannot create directory {path_accum}: a file with the same name exists"
                )
        print(repr(dir_path), os.path.exists(dir_path), os.path.isdir(dir_path))
        os.makedirs(dir_path, exist_ok=True)

    with open(src, "r") as source_file:
        content = source_file.read()
    with open(dst, "w") as dest_file:
        dest_file.write(content)

    os.remove(src)
