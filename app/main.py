import os


def move_file(command: str) -> None:
    cmd = command.split(" ")
    if len(cmd) != 3 or cmd[0] != "mv":
        return

    src_file = cmd[1]
    dst_file = cmd[2]
    if src_file == dst_file:
        return

    dst_dir = os.path.dirname(dst_file)
    if dst_dir and not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    try:
        with open(src_file, "r") as src, open(dst_file, "w") as dst:
            dst.write(src.read())
        os.remove(src_file)
    except FileNotFoundError:
        print(f"File {src_file} not found")
