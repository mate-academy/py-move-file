import os


def move_file(command: str) -> None:
    command, origin, path = command.split()

    if command == "mv":

        destination = os.path.dirname(path)
        if destination:
            os.makedirs(destination, exist_ok=True)

        with open(origin, "r") as read_file, open(path, "w") as write_file:
            write_file.write(read_file.read())

        os.remove(origin)
