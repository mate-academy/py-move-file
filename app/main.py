import os


def move_file(command: str) -> None:
    _, source, destination = command.split()

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    dest_dir = os.path.dirname(destination)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with open(source, "r") as f:
        content = f.read()

    with open(destination, "w") as f:
        f.write(content)

    os.remove(source)
