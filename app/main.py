import os


def move_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    src = parts[1]
    dest = parts[2]

    if not os.path.exists(src):
        return

    if dest.endswith("/") or dest.endswith("\\"):
        dest_dir = dest.rstrip("/\\")
        target_file = os.path.join(dest, os.path.basename(src))
    else:
        dest_dir = os.path.dirname(dest)
        target_file = dest

    if dest_dir:
        current_path = ""
        for folder in dest_dir.replace("\\", "/").split("/"):
            if folder:
                current_path = (
                    os.path.join(current_path, folder)
                    if current_path
                    else folder
                )
                if not os.path.exists(current_path):
                    os.mkdir(current_path)

    with open(src, "rb") as f_src:
        content = f_src.read()

    with open(target_file, "wb") as f_dest:
        f_dest.write(content)

    os.remove(src)
