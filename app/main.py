import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    source = parts[1]
    destination = parts[2]

    if not os.path.isfile(source):
        return

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    if source == destination:
        return

    directory = os.path.dirname(destination)
    if directory:
        path = ""
        for folder in directory.split("/"):
            path = os.path.join(path, folder)
            if not os.path.exists(path):
                os.mkdir(path)

    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(source)
