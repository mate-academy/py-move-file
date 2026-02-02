import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3:
        return
    command, src, dst = command_list
    if command != "mv":
        return
    if src == dst:
        return
    if os.path.isdir(dst):
        dst = os.path.join(dst, os.path.basename(src))
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
        with open(src, "r") as f, open(full_path, "w") as file:
            file.write(f.read())

        os.remove(src)
