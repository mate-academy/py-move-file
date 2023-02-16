import os


def move_file(command: str) -> None:
    command, file_name, directory = command.split()
    if command != "mv":
        raise ValueError("Wrong command!")
        return
    directory = directory.split("/")
    new_file = directory.pop(-1)
    path = ""
    for folder in directory:
        path += folder + "/"
        if not os.path.exists(path):
            os.mkdir(path)
    with open(file_name) as file, open(path + new_file, "w") as new:
        new.write(file.read())
    os.remove(file_name)
