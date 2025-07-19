import os


def move_file(command: str) -> None:
    args = command.split(" ")
    if len(args) != 3:
        raise ValueError("Invalid command")

    com, file, path = args
    path = path.split("/")

    if com != "mv":
        raise ValueError("Invalid command")

    if len(path) < 2:
        os.rename(file, path[0])
        return

    if not os.path.exists("/".join(path[:-1])):
        os.makedirs("/".join(path[:-1]))
    with open(file, "r") as file_to_remove:
        content = file_to_remove.read()
    os.remove(file)
    with open("/".join(path), "w") as new_file:
        new_file.write(content)
