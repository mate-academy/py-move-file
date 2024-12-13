import os


def move_file(command: str) -> None:
    command = command.split(" ")

    if command[0] != "mv":
        raise NameError("Cannot recognize the command")

    current_file = command[1]
    path_to_file = command[2].split("/")
    new_directory = "/".join(path_to_file[:-1])
    os.makedirs(new_directory)

    if path_to_file[-1] == "":
        path_to_file.append(current_file)
    path_to_file = "/".join(path_to_file)

    with open(current_file, "r") as source, \
            open(path_to_file, "a") as new_file:
        info = source.read()
        new_file.write(f"{info}")
        os.remove(current_file)
