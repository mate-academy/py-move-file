import os


def move_file(command: str) -> None:
    command = command.split()
    if command[0] != "mv":
        return None

    filename = command[1]
    path = command[2].split("/")
    new_filename = path.pop()
    path = "/".join(path)

    if path:
        os.makedirs(path)

    with open(filename, "r") as file, \
            open(path + new_filename, "w") as new_file:
        new_file.write(file.read())

    os.remove(filename)
