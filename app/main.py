import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, destination = parts

    if os.path.isdir(destination) or destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    dir_path = os.path.dirname(destination)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    with open(source, "r") as f:
        content = f.read()

    with open(destination, "w") as f:
        f.write(content)

    os.remove(source)
