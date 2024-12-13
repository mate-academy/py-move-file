import os


def move_file(command: str) -> None:
    _, source, destination = command.split()

    if not os.path.exists(source):
        raise FileNotFoundError

    if destination.endswith(os.sep):
        destination_dir = destination.rstrip(os.sep)
        destination_file = os.path.basename(source)
    else:
        destination_dir, destination_file = os.path.split(destination)

    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    os.rename(source, os.path.join(destination_dir, destination_file))
