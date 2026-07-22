import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, destination = parts

    if not os.path.isfile(source):
        return

    if destination.endswith("/"):
        destination = os.path.join(
            destination,
            os.path.basename(source),
        )

    directory = os.path.dirname(destination)

    if directory:
        current = ""
        for folder in directory.split("/"):
            current = os.path.join(current, folder)

            if not os.path.exists(current):
                os.mkdir(current)

    with open(source, "r") as file_in:
        content = file_in.read()

    with open(destination, "w") as file_out:
        file_out.write(content)

    os.remove(source)
