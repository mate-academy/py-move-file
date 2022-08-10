import os


def move_file(command: str):
    def get_dir_name(file_name: str):
        return file_name[:file_name.rfind(os.path.sep)]\
            if os.path.sep in file_name else ""

    cmd, file_name_src, file_name_dst = (command.split() + [""] * 3)[:3]

    if cmd != 'mv' or not file_name_src or not file_name_dst:
        raise ValueError("Command line is incorrect")

    if not os.path.exists(file_name_src):
        raise Exception(f"Source file '{file_name_src}' not exists")

    dir_name_src = get_dir_name(file_name_src)
    dir_name_dst = get_dir_name(file_name_dst)

    if not dir_name_src and not dir_name_dst:
        os.rename(file_name_src, file_name_dst)
    else:
        full_path = ""
        for dir_name in dir_name_dst.split(os.path.sep):
            full_path += dir_name + os.path.sep
            if not os.path.exists(full_path):
                os.mkdir(full_path, 0o777)

        with open(file_name_src, "r") as file_src,\
                open(file_name_dst, "w") as file_dst:
            file_dst.write(file_src.read())

        os.remove(file_name_src)
