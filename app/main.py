import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    if parts[0] != "mv":
        return

    _, source, destination = parts

    with open(source, "r") as file:
        text = file.read()

    if destination.endswith("/"):
        filename = os.path.basename(source)
        destination = os.path.join(destination, filename)

    directory = os.path.dirname(destination)

    if directory:
        folders = directory.split("/")

        current_path = ""

        for folder in folders:
            current_path = os.path.join(current_path, folder)

            if not os.path.exists(current_path):
                os.mkdir(current_path)

    with open(destination, "w") as file:
        file.write(text)

    os.remove(source)
