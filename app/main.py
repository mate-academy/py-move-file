import os


def move_file(command: str) -> None:
    _, source, destination = command.split()

    directories, _, filename = destination.rpartition("/")

    if directories:
        os.makedirs(directories, exist_ok=True)

    if not filename:
        filename = os.path.basename(source)

    destination_path = os.path.join(directories, filename)

    with open(source, "r") as src_file:
        content = src_file.read()

    with open(destination_path, "w") as dest_file:
        dest_file.write(content)

    os.remove(source)
