import os


def move_file(command: str) -> None:

    parts = command.split()

    if len(parts) == 3 and parts[0] == "mv":
        src, final_dst = parts[1], parts[2]
        sorce_file_name = os.path.basename(src)

        if final_dst.endswith(os.sep):
            final_dst = os.path.join(final_dst, sorce_file_name)
            create_dir(final_dst)
            with open(src, "r") as sorce:
                with open(final_dst, "w") as dest:
                    dest.write(sorce.read())
            os.remove(src)
        else:
            create_dir(final_dst)
            with open(src, "r") as sorce:
                with open(final_dst, "w") as dest:
                    dest.write(sorce.read())
            os.remove(src)


def create_dir(final_dst: str) -> None:

    paths = os.path.dirname(final_dst)
    paths = os.path.normpath(paths)
    paths = paths.split(os.sep)
    current = ""
    for path in paths:
        if path in ("", "."):
            continue
        if not current:
            current = path
        elif current:
            current = os.path.join(current, path)
        try:
            os.mkdir(current)
        except (FileExistsError):
            continue
