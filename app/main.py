import os


def move_file(command: str) -> None:
    _, source, destination = command.split()

    if destination.endswith("/"):
        destination += os.path.basename(source)

    destination_dir = os.path.dirname(destination)

    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    with open(source, "r") as source_file:
        content = source_file.read()

    with open(destination, "w") as destination_file:
        destination_file.write(content)

    os.remove(source)
