import os


def move_file(command: str) -> None:
    _, old_name, directory = command.split()

    if _ == "mv":
        path, new_file = os.path.split(directory)

        if not os.path.exists(path) and path != "":
            os.makedirs(name=path)

        with open(old_name, "r") as old:
            with open(directory, "w") as new:
                new.write(old.read())

        os.remove(old_name)
