import os


def move_file(command: str) -> None:
    parts = command.split()
    source = parts[1]
    destination = parts[2]
    if destination.endswith("/"):
        destination += os.path.basename(source)
    directory = os.path.dirname(destination)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    with open(source, "r") as file:
        content = file.read()
    with open(destination, "w") as file:
        file.write(content)
    os.remove(source)
