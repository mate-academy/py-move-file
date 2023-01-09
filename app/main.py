import os


def move_file(command: str) -> None:
    short_command = command.split()[0]
    source = command.split()[1]
    path = command.split()[2]
    if short_command != "mv":
        return
    if "/" not in path:
        os.rename(source, path)
        return
    path_parts = path.split("/")[:-1]
    filename = path.split("/")[-1]
    path = ""
    for part in path_parts:
        path = os.path.join(path, part)
    os.makedirs(path, exist_ok=True)
    filepath = os.path.join(path, filename)
    with open(filepath, "w") as new_file, open(source, "r") as copy_from:
        new_file.write(copy_from.read())
    os.remove(source)
