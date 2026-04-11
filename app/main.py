import os


def move_file(command: str) -> None:
    cmd, src, dst = command.split()
    if len(command.split()) == 3 and cmd == "mv":
        if "/" in dst:
            if os.path.isdir(dst):
                raise FileExistsError
            directory = os.path.dirname(dst)
            os.makedirs(directory, exist_ok=True)
        with open(src, "r") as file_in, \
                open(dst, "w") as file_out:
            file_out.write(file_in.read())
        os.remove(src)
