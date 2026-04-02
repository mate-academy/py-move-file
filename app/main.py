import os


def move_file(command: str) -> None:
    comm = command.split()
    if len(comm) != 3 or comm[0] != "mv":
        return
    action, source, destination = comm

    if destination.endswith("/"):
        final = os.path.join(destination, os.path.basename(source))
    else:
        final = destination

    parent = os.path.dirname(final)
    if parent:
        os.makedirs(parent, exist_ok=True)

    with open(source, "r") as file_in:
        content = file_in.read()

    with open(final, "w") as file_out:
        file_out.write(content)

    os.remove(source)
