import os


def move_file(mv_file: str) -> None:
    create_list = mv_file.split()
    if len(create_list) != 3 or create_list[0] != "mv":
        raise FileNotFoundError
    src = create_list[1]
    dst = create_list[-1]
    create_folder = dst.strip("/").split("/")
    if dst.endswith("/"):
        path_folder = create_folder
        file_name = os.path.basename(src)
    else:
        path_folder = create_folder[:-1]
        file_name = create_folder[-1]
    current_path = ""
    for folder in path_folder:
        current_path = os.path.join(current_path, folder)
        if not os.path.exists(current_path):
            os.mkdir(current_path)
    if os.path.exists(current_path):
        with open(src, "r") as read_file, open(current_path + "/" + file_name, "w") as create_file:
            create_file.write(read_file.read())
            os.remove(src)
    with open(src, "r") as read_file, open(dst, "w") as create_file:
        create_file.write(read_file.read())
        if src != dst:
            os.remove(src)