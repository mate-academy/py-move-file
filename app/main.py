import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    source = parts[1]
    destination = parts[2]

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination += source.split("/")[-1]
    else:
        folder = os.path.dirname(destination)

        if folder:
            os.makedirs(folder, exist_ok=True)

    with open(source, "r") as file:
        text = file.read()

    with open(destination, "w") as file:
        file.write(text)

    os.remove(source)
