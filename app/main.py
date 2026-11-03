import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, destination = parts

    if destination.endswith("/"):
        filename = os.path.basename(source)
        destination = os.path.join(destination, filename)

    if os.path.abspath(source) == os.path.abspath(destination):
        return

    directory = os.path.dirname(destination)
    missing_dirs = []

    while directory and not os.path.exists(directory):
        missing_dirs.append(directory)
        directory = os.path.dirname(directory)

    for path in reversed(missing_dirs):
        os.mkdir(path)

    with open(source, "rb") as file_in, open(destination, "wb") as file_out:
        file_out.write(file_in.read())

    os.remove(source)
