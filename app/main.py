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

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination += source.split("/")[-1]
    else:
        folder = os.path.dirname(destination)

        if folder:
            os.makedirs(folder, exist_ok=True)

    with open(source, "r") as file:
        content = file.read()

    with open(destination, "w") as file:
        file.write(content)

    os.remove(source)
