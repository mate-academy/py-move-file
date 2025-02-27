import os


def move_file(command: str) -> None:
    if not command.startswith("mv"):
        return

    args = command.split()[1:]
    if len(args) != 2 or args[0] is None or args[1] is None:
        return

    src_name, dst_name = args
    dst_folder = os.path.dirname(dst_name)
    if not dst_folder:
        os.rename(src_name, dst_name)
        return

    os.makedirs(dst_folder, exist_ok=True)

    try:
        with (open(src_name, "r") as src_file,
              open(dst_name, "w") as dst_file):
            dst_file.write(src_file.read())
    except FileNotFoundError:
        return

    os.remove(src_name)
