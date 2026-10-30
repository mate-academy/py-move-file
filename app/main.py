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
        directories = path.split("/")
        current_dir = ""
        for directory in directories:
            if not directory:
                continue
            current_dir = os.path.join(current_dir, directory) if current_dir else directory
            try:
                os.mkdir(current_dir)
            except FileExistsError:
                pass

    with open(source, "r") as root, open(destination, "w") as dest_path:
        dest_path.write(root.read())

    os.remove(source)
