import os


def move_file(command: str) -> None:
    command_line = command.split()
    if len(command_line) != 3 or command_line[0] != "mv":
        return
    src = command_line[1]
    dest = command_line[2]
    if src == dest:
        return
    try:
        if dest.endswith("/"):
            filename = os.path.basename(src)
            dest = os.path.join(dest, filename)
        dir_path = os.path.dirname(dest)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
        with open(src, "r") as src_file:
            content = src_file.read()
        with open(dest, "w") as dest_file:
            dest_file.write(content)
        os.remove(src)
    except FileNotFoundError:
        pass
