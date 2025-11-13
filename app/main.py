import os


def move_file(mv_file: str) -> None:
    create_list = mv_file.split()
    if len(create_list) != 3:
        raise FileNotFoundError
    if create_list[0] != "mv":
        raise ValueError
    src = create_list[1]
    dst = create_list[-1]
    if not os.path.isfile(src):
        raise FileNotFoundError
    if "/" not in dst:
        with open(src, "r") as read_file, open(dst, "w") as create_file:
            create_file.write(read_file.read())
            if os.path.normpath(src) != os.path.normpath(dst):
                os.remove(src)
    else:
        create_folder = dst.strip("/").split("/")
        target_name = create_folder[-1]
        current_path = ""
        for folder in create_folder[:-1]:
            current_path = os.path.join(current_path, folder)
            if not os.path.exists(current_path):
                os.mkdir(current_path)
        if os.path.exists(current_path):
            if dst.endswith("/"):
                target_name = os.path.basename(src)
            else:
                target_name = os.path.basename(dst)
            if not os.path.isfile(src):
                raise FileNotFoundError
            with open(src, "r") as r, open(os.path.join(current_path, target_name), "w") as w:
                w.write(r.read())
                os.remove(src)
