import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, destination = parts

    if not os.path.exists(source):
        return

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    destination = os.path.normpath(destination)
    directories = destination.split(os.sep)[:-1]
    current_path = ""
    for directory in directories:
        current_path = os.path.join(current_path, directory)
        if not os.path.exists(current_path):
            os.mkdir(current_path)

    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(source)
