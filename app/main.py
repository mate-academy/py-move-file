import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return
    _, source, destination = parts

    if destination.endswith("/"):
        destination = os.path.join(
            destination,
            os.path.basename(source)
        )

    directory = os.path.dirname(os.path.normpath(destination))

    if directory:
        current_directory = ""

        for part in directory.split(os.sep):
            current_directory = os.path.join(current_directory, part)

            if not os.path.exists(current_directory):
                os.mkdir(current_directory)

    with open(source, "r") as file:
        content = file.read()
    with open(destination, "w") as file:
        file.write(content)
    os.remove(source)
