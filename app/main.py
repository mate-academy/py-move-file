import os


def move_file(command: str) -> None:
    cmd = command.split()

    if len(cmd) != 3 or cmd[0] != "mv":
        return

    source = cmd[1]
    destination = cmd[2]

    if not os.path.isfile(source):
        return

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        directory = os.path.dirname(destination)
        if directory:
            os.makedirs(directory, exist_ok=True)

    with open(source, "rb") as src, open(destination, "wb") as dst:
        dst.write(src.read())

    os.remove(source)
