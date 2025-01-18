import os


def move_file(command: str) -> None:
    _, source, destination = command.split()

    if not os.path.exists(source):
        raise FileNotFoundError(f"{source} does not exist")

    dest_dir = os.path.dirname(destination)

    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    os.rename(source, destination)

    if os.path.exists(source):
        os.remove(source)
