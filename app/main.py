import os


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "mv":
        return

    src = command_parts[1]
    dst = command_parts[2]

    if not os.path.isfile(src):
        return

    ends_with_sep = command.rstrip().endswith(("/", "\\"))
    if ends_with_sep or os.path.isdir(dst):
        dst_dir = dst.rstrip("/\\")
        if dst_dir == "":
            dst_dir = "."
        os.makedirs(dst_dir, exist_ok=True)
        dst = os.path.join(dst_dir, os.path.basename(src))
    else:
        dir_path = os.path.dirname(dst)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

    if src == dst:
        return

    try:
        os.rename(src, dst)
    except OSError:
        with (open(src, "r", encoding="utf-8") as original_file,
              open(dst, "w", encoding="utf-8") as new_file):
            for line in original_file:
                new_file.write(line)
        os.remove(src)
