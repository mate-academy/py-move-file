import os


def move_file(command: str) -> None:
    parts = command.strip().split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command")

    source = parts[1]
    destination = parts[2]

    if not os.path.isfile(source):
        raise FileNotFoundError(f"No such file: '{source}'")

    def make_dirs(path: str) -> None:
        if not path or os.path.isdir(path):
            return

        parent = os.path.dirname(path)

        if parent:
            make_dirs(parent)

        if not os.path.isdir(path):
            os.mkdir(path)

    if destination.endswith("/"):
        target_path = os.path.join(destination, os.path.basename(source))
        target_dir = destination
    else:
        target_path = destination
        target_dir = os.path.dirname(destination)

    if os.path.abspath(source) == os.path.abspath(target_path):
        return

    if target_dir:
        make_dirs(target_dir)

    with open(source, "rb") as f:
        content = f.read()

    with open(target_path, "wb") as f:
        f.write(content)

    os.remove(source)
