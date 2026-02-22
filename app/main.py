import os


def move_file(command: str) -> None:
    command_ls = command.split()

    if len(command_ls) == 3 and command_ls[0] == "mv":
        source = command_ls[1]
        dest = command_ls[2]
    else:
        return

    if dest.endswith("/") or os.path.isdir(dest):
        dest_full = os.path.join(dest, os.path.basename(source))
    else:
        dest_full = dest

    dirname = os.path.dirname(dest_full)
    if dirname != "":
        curr = ""
        normalized_dirname = dirname.replace("\\", "/")
        for part in normalized_dirname.split("/"):
            if not part and not curr:
                curr = os.sep
                continue
            curr = os.path.join(curr, part) if curr else part
            if not os.path.exists(curr):
                os.mkdir(curr)

    if not os.path.isfile(source):
        return

    with open(source, "rb") as f_src:
        with open(dest_full, "wb") as f_dst:
            while chunk := f_src.read(1024 * 1024):
                f_dst.write(chunk)
    os.remove(source)
