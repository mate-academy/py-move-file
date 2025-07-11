import os


def move_file(command: str) -> None:
    try:
        action, src_file, dest_file = command.split()
    except ValueError:
        return

    if src_file == dest_file or action != "mv":
        return

    try:
        with open(src_file, "r") as f:
            data = f.read()
    except FileNotFoundError:
        return
    os.remove(src_file)

    path = "/".join(dest_file.split("/")[:-1])
    try:
        # raise FileNotFoundError if path is clear
        # (additional dictionary is not needed)
        os.makedirs(path, exist_ok=True)
    except FileNotFoundError:
        pass

    with open(dest_file, "w") as f:
        f.write(data)
