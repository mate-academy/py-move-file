import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return
    source, destination = parts[1], parts[2]
    if not os.path.exists(source):
        return
    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))
    if os.path.exists(destination):
        return
    dir_path = os.path.dirname(destination)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)
    os.rename(source, destination)
