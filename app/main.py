import os


def move_file(command: str) -> None:
    _, src, dst = command.split()
    dst_folder, dst_filename = os.path.split(dst)

    if dst_folder:
        os.makedirs(dst_folder, exist_ok=True)

    new_file = dst
    with open(src, "r") as file_read, \
            open(new_file, "w") as file_write:
        text = file_read.read()
        file_write.write(text)
    os.remove(src)
