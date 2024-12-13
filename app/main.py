import os


def move_file(command: str) -> None:
    flag, old_name, directory = command.split()

    if flag == "mv":
        path, new_file = os.path.split(directory)

        if path != "":
            os.makedirs(name=path, exist_ok=True)

        with open(old_name, "r") as old, open(directory, "w") as new:
            new.write(old.read())

        os.remove(old_name)
