import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, destination = parts

    if source == destination:
        return

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))
    else:
        directory = os.path.dirname(destination)

        if directory:
            os.makedirs(directory, exist_ok=True)

    with open(source, "rb") as file_in, open(destination, "wb") as file_out:
        file_out.write(file_in.read())

    os.remove(source)
