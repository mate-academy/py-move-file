import os


def move_file(command: str) -> None:
    tokens = command.split(" ")

    if len(tokens) != 3:
        return

    command = tokens[0]
    name_of_original = tokens[1]
    name_of_moved = tokens[2]

    if (
        not os.path.exists(name_of_original)
        or command != "mv"
        or name_of_original == name_of_moved
    ):
        return

    directories = name_of_moved.split("/")[:-1]
    path = ""

    for directory in directories:
        path = os.path.join(path, directory)

        if not os.path.exists(path):
            os.mkdir(path)

    with (
        open(name_of_original, "r") as file_in,
        open(name_of_moved, "w") as file_out
    ):
        file_out.write(file_in.read())

    os.remove(name_of_original)
