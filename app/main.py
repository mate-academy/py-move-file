import os


def move_file(command: str) -> None:
    cmd = command.split()

    if len(cmd) != 3 or cmd[0] != "mv":
        return

    source = cmd[1]
    destination = cmd[2]

    if destination.endswith("/"):
        dest_dir = destination.rstrip("/")
        if not os.path.isdir(dest_dir):
            os.makedirs(dest_dir)
        destination = os.path.join(dest_dir, os.path.basename(source))
    else:
        directory = os.path.dirname(destination)
        if directory and not os.path.isdir(directory):
            os.makedirs(directory)

    with open(source, "r") as src, open(destination, "w") as dst:
        dst.write(src.read())

    os.remove(source)
