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

    directories, _ = os.path.split(dest_file)
    if directories:
        os.makedirs(directories, exist_ok=True)

    with open(dest_file, "w") as f:
        f.write(data)
