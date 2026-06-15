import os


def move_file(command: str) -> None:
    _, source, destination = command.split()

    if destination.endswith("/"):
        destination = destination + os.path.basename(source)

    dest_dir = os.path.dirname(destination)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(source, "r") as src_file:
        content = src_file.read()

    with open(destination, "w") as dest_file:
        dest_file.write(content)

    os.remove(source)
