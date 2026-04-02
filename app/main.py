import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command forman")

    source = parts[1]
    destination = parts[2]

    if not os.path.isfile(source):
        raise ValueError(f"Source file '{source}' does not exist.")

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        dest_dir = os.path.dirname(destination)
        if dest_dir:
            os.makedirs(dest_dir, exist_ok=True)

    with open(source, "rb") as src_file:
        with open(destination, "wb") as dest_file:
            dest_file.write(src_file.read())

    os.remove(source)
