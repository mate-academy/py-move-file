import os


def move_file(command: str) -> None:
    try:
        trash, source, destination = command.split()
    except ValueError:
        return
    if trash != "mv" or not source or not destination:
        return
    if source == destination:
        return
    if destination.endswith("\\") or destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))
    else:
        destination = os.path.normpath(destination)
    if os.path.dirname(destination) != "":
        os.makedirs(os.path.dirname(destination), exist_ok=True)
    os.rename(source, destination)
