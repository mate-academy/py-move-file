import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, destination = parts

    source = os.path.normpath(source)
    destination = os.path.normpath(destination)

    if not os.path.isfile(source):
        return

    if source == destination:
        return

    if command.endswith(("/", "\\")) or os.path.isdir(destination):
        filename = os.path.basename(source)
        destination = os.path.join(destination, filename)

    directory = os.path.dirname(destination)
    if directory:
        os.makedirs(directory, exist_ok=True)

    try:
        with open(source, "rb") as file_in:
            content = file_in.read()
        with open(destination, "wb") as file_out:
            file_out.write(content)
        os.remove(source)
    except (OSError, IOError):
        pass
