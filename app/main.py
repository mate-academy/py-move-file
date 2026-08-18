import os


def move_file(command: str) -> None:
    spl_cmd = command.split()
    if len(spl_cmd) == 3 and spl_cmd[0] == "mv":
        _, src_file_name, addr = spl_cmd
        dest_file_name = os.path.basename(addr)
        path = os.path.dirname(addr)

        if not dest_file_name:
            dest_file_name = os.path.basename(src_file_name)

        if path:
            os.makedirs(path, exist_ok=True)

        try:
            with (open(src_file_name, "r") as src,
                  open(os.path.join(path, dest_file_name), "w") as dest):
                dest.write(src.read())
                os.remove(src_file_name)
        except FileNotFoundError:
            pass
