import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command")

    _, source, destination = parts

    if destination.endswith("/"):
        destination = os.path.join(
            destination,
            os.path.basename(source),
        )

    destination_dir = os.path.dirname(destination)

    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    with open(source, "r") as source_file:
        content = source_file.read()

    with open(destination, "w") as destination_file:
        destination_file.write(content)

    os.remove(source)
