import os


def move_file(command: str) -> None:
    if len(command.split()) == 3 and command.split()[0] == "mv":
        addr = command.split()[2]
        src_file_name = command.split()[1]
        dest_file_name = os.path.basename(addr)
        path = os.path.dirname(addr)

        if not dest_file_name:
            dest_file_name = src_file_name

        if path:
            os.makedirs(path, exist_ok=True)

        try:
            with (open(src_file_name, "r") as src,
                  open(os.path.join(path, dest_file_name), "w") as dest):
                dest.write(src.read())
                os.remove(src_file_name)
        except FileNotFoundError:
            pass
