import os


def move_file(command: str) -> None:
    _, source, destination = command.split()

    if destination.endswith("/"):
        destination = (
            destination
            + os.path.basename(source)
        )

    directory = os.path.dirname(destination)

    if directory:
        os.makedirs(
            directory,
            exist_ok=True,
        )

    with open(source, "rb") as src:
        data = src.read()

    with open(destination, "wb") as dst:
        dst.write(data)

    os.remove(source)
