import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    action, source, destination = parts

    if action != "mv" or not os.path.isfile(source):
        return

    if destination.endswith("/") or os.path.isdir(destination):
        destination = os.path.join(destination, os.path.basename(source))

    if os.path.abspath(source) == os.path.abspath(destination):
        return

    directory = os.path.dirname(destination)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with (
        open(source, "rb") as file_in,
        open(destination, "wb") as file_out,
    ):
        file_out.write(file_in.read())

    os.remove(source)
