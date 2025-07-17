import os


def move_file(command: str) -> None:
    parts = command.strip().split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError

    _, source, destination = parts

    if not os.path.isfile(source):
        raise FileNotFoundError(f"Source file '{source}' does not exist.")

    destination_dir = os.path.dirname(destination)
    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    with open(source, "rb") as f_source:
        content = f_source.read()

    with open(destination, "wb") as f_destination:
        f_destination.write(content)

    os.remove(source)
