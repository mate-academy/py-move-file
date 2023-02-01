import os


def move_file(command: str) -> None:
    cmd, src, dst = command.split()
    if cmd == "mv":
        source_file = src
        new_file = dst
        if "/" in dst:
            current_path = os.path.dirname(dst)
            os.makedirs(current_path, exist_ok=True)
            new_file = os.path.basename(dst)
            new_file = os.path.join(current_path, new_file)
        with open(source_file, "r") as file_read, \
                open(new_file, "w") as file_write:
            text = file_read.read()
            file_write.write(text)
        os.remove(source_file)
