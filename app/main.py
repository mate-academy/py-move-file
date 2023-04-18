import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        return
    command_name, origin_file, path_file = command.split()
    if command_name != "mv":
        return
    if path_file.count("/") > 0:
        os.makedirs(os.path.dirname(path_file), exist_ok=True)
    with open(origin_file, "r") as origin, open(path_file, "w") as copy:
        copy.write(origin.read())
    os.remove(origin_file)
