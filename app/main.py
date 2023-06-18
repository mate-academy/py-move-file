import os


def move_file(command: str) -> None:

    if len(command.split()) == 3:
        mv, origin, path = command.split()

        if mv == "mv":
            destination = os.path.dirname(path)
            if destination:
                os.makedirs(destination, exist_ok=True)

        with open(origin, "r") as read_file, open(path, "w") as write_file:
            write_file.write(read_file.read())

        os.remove(origin)
