import os


def move_file(command: str) -> None:
    if command == "":
        return

    list_of_files = command.strip().split()
    if list_of_files[0] != "mv" or len(list_of_files) != 3:
        return
    _, source, destination = list_of_files

    if not os.path.isfile(source):
        return

    if destination.endswith(os.sep):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        dest_dir = os.path.dirname(destination)
        if dest_dir:
            os.makedirs(dest_dir, exist_ok=True)

    if os.path.exists(destination):
        os.remove(destination)

    os.rename(source, destination)
