import os


def move_file(command: str) -> None:
    command_list = command.split()

    if command_list[0] != "mv":
        raise SyntaxError("Unknown command!")

    with open(command_list[1], "r") as old_file:
        info = old_file.read()
    os.remove(command_list[1])

    path = command_list[2].split("/")

    for folder in path[:-1]:
        if not os.path.isdir(folder):
            os.mkdir(folder)
        os.chdir(folder)

    with open(path[-1], "w") as new_file:
        new_file.write(info)
