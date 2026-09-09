import os


def move_file(command: str) -> None:
    """
    Move a file from source to destination.

    Args:
        command(str): The command string
        containing the source and destination paths.
    """
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, destination = parts

    if not os.path.isfile(source):
        return

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)

        filename = os.path.basename(source)
        destination = os.path.join(destination, filename)
    else:
        folder = os.path.dirname(destination)

        if folder:
            os.makedirs(folder, exist_ok=True)

    with open(source, "r") as file:
        content = file.read()

    with open(destination, "w") as file:
        file.write(content)

    os.remove(source)
