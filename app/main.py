import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, destination = parts

    if destination.endswith("/"):
        destination += source.split("/")[-1]

    directories = destination.split("/")[:-1]

    current_path = ""

    for directory in directories:
        current_path = os.path.join(current_path, directory)

        if not os.path.exists(current_path):
            os.mkdir(current_path)

    with open(source, "rb") as source_file:
        content = source_file.read()

    with open(destination, "wb") as destination_file:
        destination_file.write(content)

    os.remove(source)
