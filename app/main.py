import os


folder_path = "/dir"


def move_file(command: str) -> None:
    splitted = command.split()

    if splitted[0] != "mv":
        return

    mv_split, source, destination = splitted

    if os.path.isdir(destination):
        filename = os.path.basename(source)
        destination = os.path.join(destination, filename)

    dest_dir = os.path.dirname(destination)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    os.rename(source, destination)
