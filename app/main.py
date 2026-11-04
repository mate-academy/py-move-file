import os


def move_file(command: str) -> None:
    parts = command.split()
    source = parts[1]
    destination = parts[2]

    if destination.endswith("/"):
        destination = destination + os.path.basename(source)

    directory = os.path.dirname(destination)
    if directory:
        path = ""
        for folder in directory.split("/"):
            path = os.path.join(path, folder)
            if not os.path.exists(path):
                os.mkdir(path)

    with open(source) as f:
        content = f.read()
    with open(destination, "w") as f:
        f.write(content)
    os.remove(source)
