import os


def move_file(command: str) -> None:
    cmd, src, dst = command.split()
    if cmd == "mv":
        source_file = src
        source_folder, source_filename = os.path.split(src)
        dst_folder, dst_filename = os.path.split(dst)

        if dst_folder:
            os.makedirs(dst_folder, exist_ok=True)

        new_file = os.path.join(dst_folder, dst_filename)
        with open(source_file, "r") as file_read, \
                open(new_file, "w") as file_write:
            text = file_read.read()
            file_write.write(text)
        os.remove(source_file)
