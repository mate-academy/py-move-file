import os


def move_file(command: str) -> None:

    if len(command.split()) != 3 or command.split()[0] != "mv":
        raise ValueError
    command_name, source_file, destination = command.split()

    if not os.path.isfile(source_file):
        raise FileNotFoundError

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source_file))
    else:
        dest_dir = os.path.dirname(destination)
        if dest_dir:
            os.makedirs(dest_dir, exist_ok=True)

    with open(source_file, "r") as source:
        with open(destination, "w") as dest:
            dest.write(source.read())

    os.remove(source_file)
