import os


def move_file(command: str) -> None:
    path_parts = command.split()

    if len(path_parts) != 3 or path_parts[0] != "mv":
        raise ValueError("Invalid command format")

    source = path_parts[1]
    destination = path_parts[2]

    dir_path = os.path.dirname(destination)
    dir_parts = dir_path.split("/")
    current_path = ""

    if destination.endswith("/"):
        filename = os.path.basename(source)
        os.makedirs(dir_path, exist_ok=True)
        destination = os.path.join(destination, filename)

    for part in dir_parts:
        if not part:
            continue
        current_path = os.path.join(current_path, part)
        if not os.path.exists(current_path):
            os.mkdir(current_path)

    with open(source, "r") as src:
        content = src.read()
    with open(destination, "w") as dst:
        dst.write(content)
    os.remove(source)
