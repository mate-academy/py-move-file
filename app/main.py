import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, destination = parts

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    if source == destination:
        return

    directory = os.path.dirname(destination)

    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(source, "r") as file_in:
        content = file_in.read()

    with open(destination, "w") as file_out:
        file_out.write(content)

    os.remove(source)
