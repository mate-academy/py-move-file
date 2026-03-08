import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) != 3:
        return
    source, destination = command[1], command[2]

    if destination.endswith("/"):
        final = os.path.join(destination, os.path.basename(source))
    else:
        final = destination

    parent = os.path.dirname(final)
    if parent:
        os.makedirs(parent, exist_ok=True)
    os.replace(source, final)
