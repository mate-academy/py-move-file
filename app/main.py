import os


def move_file(command: str) -> None:
    command, file_before, direction = command.split()
    if command != "mv":
        raise ValueError("Wrong command")

    path, new_file = os.path.split(direction)

    if not os.path.exists(path) and path != "":
        os.makedirs(name=path)

    with open(file_before, "r") as old_file, open(direction, "w") as file:
        file.write(old_file.read())
    os.remove(file_before)
