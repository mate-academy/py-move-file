from os import remove
from pathlib import Path


def move_file(command: str) -> None:

    command = command.split(" ")

    if len(command) != 3 or command[0] != "mv":
        return

    source = command[1]
    dest = command[2]

    if source == dest:
        return

    try:
        path = Path("/".join(dest.split("/")[:-1]))
        path.mkdir(parents=True, exist_ok=True)

        with open(source, "r") as src_file, open(dest, "w") as dest_file:
            dest_file.write(src_file.read())
            src_file.close()
            remove(source)
    except FileNotFoundError:
        return
