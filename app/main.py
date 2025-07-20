import os


def move_file(command: str) -> None:
    args = command.split(" ")
    if len(args) != 3:
        raise ValueError("Invalid command")

    com, file, path = args
    path = path.split("/")

    if com != "mv":
        raise ValueError("Invalid command")

    if len(path) < 2:
        os.rename(file, path[0])
        return

    dest_dir = os.path.dirname("/".join(path))
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    os.rename(file, "/".join(path))
