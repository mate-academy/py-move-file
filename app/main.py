import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, destination = parts

    directory_path = os.path.dirname(destination)

    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    with open(source, "r") as src_file:
        content = src_file.read()

    with open(destination, "w") as dest_file:
        dest_file.write(content)

    os.remove(source)
