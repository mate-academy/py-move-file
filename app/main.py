import os


def move_file(command: str) -> None:
    command, file_before, direction = command.split()
    direction = direction.split("/")
    new_file = direction.pop(-1)
    path = ""

    for directory in direction:
        path += directory + "/"
        if not os.path.exists(path):
            os.mkdir(path)

    with open(file_before) as old_file, open(path + new_file, "w") as file:
        file.write(old_file.read())
    os.remove(file_before)
