import os


def move_file(command: str) -> None:
    com_name, path_out, path_in = command.split()
    if com_name == "mv":
        if os.path.exists(path_out):
            if path_in[len(path_in) - 1] != "/":
                if "/" in path_in:
                    directories = path_in.split("/")
                    if not os.path.exists("/".join(
                            directories[:len(directories) - 1])
                    ):
                        for idx in range(1, len(directories)):
                            path = "/".join(directories[:idx])
                            if not os.path.exists(path):
                                os.mkdir(path)
                with (open(path_out) as take_file,
                      open(path_in , "w") as put_file):
                    content = take_file.read()
                    put_file.write(content)
                    os.remove(path_out)
