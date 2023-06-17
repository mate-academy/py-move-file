import os


def move_file(command: str) -> None:
    command, origin, path = command.split()

    if command == "mv":

        destination = os.path.dirname(path)
        if destination:
            if not os.path.exists(destination):
                os.makedirs(destination)

        with open(origin, "r") as f_out, open(path, "w") as f_in:
            f_in.write(f_out.read())

        os.remove(origin)
