import os


def move_file(command: str) -> None:
    _, source, destination = command.split()

    if destination.endswith("/"):
        destination += source.split("/")[-1]

    with open(source, "r") as source_file:
        content = source_file.read()

    directories = destination.split("/")[:-1]
    current_path = ""

    for directory in directories:
        current_path += directory + "/"
        if not os.path.exists(current_path):
            os.mkdir(current_path)

    with open(destination, "w") as new_file:
        new_file.write(content)

    os.remove(source)
