import os


def move_file(command: str) -> None:
    command_list = command.split()
    command, src, dst = command_list
    if len(command_list) != 3 or command != "mv":
        return
    if src == dst:
        return
    if os.path.isfile(src) and os.path.dirname(dst) == "":
        os.rename(src, dst)
        return
    if dst.endswith(os.sep):
        dst = os.path.join(dst, os.path.basename(src))
    dir_path = os.path.dirname(dst)
    file_name = os.path.basename(dst)

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
        full_path = os.path.join(dir_path, file_name)
        with (open(full_path, "w") as f, open(src, "r") as file):
            f.write(file.read())

        os.remove(src)
