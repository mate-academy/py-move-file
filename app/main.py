import os.path


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, destination = parts

    if not os.path.exists(source):
        return

    if destination.endswith("/"):
        filename = os.path.basename(source)
        destination = os.path.join(destination, filename)

    path = os.path.dirname(destination)
    if path:
        os.makedirs(path, exist_ok=True)

    with open(source, "r") as root, open(destination, "w") as dest_path:
        dest_path.write(root.read())

    os.remove(source)
