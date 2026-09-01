import os


def move_file(command: str) -> None:
    splitted = command.split()

    if splitted[0] != "mv" or len(splitted) < 3:
        return

    source = splitted[1]

    destination = splitted[2]

    if destination.endswith("/"):
        destination = destination + source

    splitted_destination = destination.split("/")

    destination_str = "/".join(splitted_destination[0:-1])

    parts = destination_str.split("/")
    for i in range(len(parts)):
        print("|||||||||||||||||||||||||||||||||")
        part = "/".join(parts[: i + 1])
        print("part ---- -- - - - ", part)
        try:
            os.mkdir(part)
        except FileNotFoundError:
            pass
        except FileExistsError:
            pass

    if os.path.isdir("/dir"):
        print("The directory exists!")

    os.rename(source, destination)
