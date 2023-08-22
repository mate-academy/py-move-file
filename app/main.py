import os


def move_file(command: str) -> None:
    args = command.split()[1:]
    source = args[0]
    destination = args[1]

    if not os.path.isfile(source):
        return

    dest_directory = os.path.dirname(destination)
    if dest_directory and not os.path.exists(dest_directory):
        os.makedirs(dest_directory)

    os.rename(source, destination)
