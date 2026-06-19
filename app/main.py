import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    source = parts[1]
    destination = parts[2]

    if destination.endswith("/"):
        file_name = os.path.basename(source)
        destination = os.path.join(destination, file_name)

    directory = os.path.dirname(destination)

    current_path = ""
    for folder in directory.split("/"):
        if folder:
            current_path = os.path.join(current_path, folder)
            if not os.path.exists(current_path):
                os.mkdir(current_path)

    with open(source, "r") as src:
        content = src.read()

    with open(destination, "w") as dst:
        dst.write(content)

    os.remove(source)
