import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Invalid command format. Expected: 'mv src_file dst_file'"
        )

    command_name, src, dst = parts

    if dst.endswith("/") or dst.endswith(os.sep):
        dst = os.path.join(dst, os.path.basename(src))

    dir_path = os.path.dirname(dst)

    if dir_path:
        sub_dirs = dir_path.split(os.sep)\
            if os.sep in dir_path else dir_path.split("/")
        current_path = ""
        for folder in sub_dirs:
            if folder:
                current_path = os.path.join(current_path, folder)\
                    if current_path else folder
                if not os.path.exists(current_path):
                    os.mkdir(current_path)

    with open(src, "rb") as f_src:
        content = f_src.read()

    with open(dst, "wb") as f_dst:
        f_dst.write(content)

    os.remove(src)
