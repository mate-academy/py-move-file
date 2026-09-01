import os
import shutil


def move_file(command: str) -> None:
    splitted = command.split()

    if splitted[0] != "mv" or len(splitted) < 3:
        return

    source = splitted[1]

    destination = splitted[2]

    if destination.endswith("/"):
        os.path.join(destination, source)

    splitted_destination = destination.split("/")

    destination_str = "/".join(splitted_destination[0:-1])

    parts = destination_str.split("/")
    for i in range(len(parts)):
        part = "/".join(parts[: i + 1])
        try:
            os.mkdir(part)
        except FileNotFoundError:
            pass
        except FileExistsError:
            pass

    shutil.copy2(source, destination)
    os.remove(source)
