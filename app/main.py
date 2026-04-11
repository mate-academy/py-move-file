import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3 and command_list[0] == "mv":
        cmd, src, dst = command_list
        if os.path.isdir(dst) or dst.endswith("/"):
            os.makedirs(dst, exist_ok=True)
            dst = os.path.join(dst, os.path.basename(src))
        else:
            directory = os.path.dirname(dst)
            if directory:
                os.makedirs(directory, exist_ok=True)
        with open(src, "r") as file_in, \
                open(dst, "w") as file_out:
            file_out.write(file_in.read())
        os.remove(src)
