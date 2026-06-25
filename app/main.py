import os


def move_file(command: str) -> None:
    cmd = command.split(" ")
    if len(cmd) != 3 or cmd[0] != "mv":
        return

    src_path = cmd[1]
    dst_path = cmd[2]
    if src_path == dst_path:
        return

    dst_dir = dst_path.split("/")[:-1]
    dst_file = dst_path.split("/")[-1]

    current_path = ""
    for path in dst_dir:
        if current_path:
            current_path = os.path.join(current_path, path)
        else:
            current_path = path

        try:
            os.mkdir(current_path)
        except FileExistsError:
            print(f"Directory {current_path} already exists")

    dst_file_path = (
        os.path.join(current_path, dst_file)
    ) if current_path else dst_file

    try:
        with open(src_path, "r") as src, open(dst_file_path, "w") as dst:
            dst.write(src.read())
        os.remove(src_path)
    except FileNotFoundError:
        print(f"File {src_path} not found")
