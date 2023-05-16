import os


def move_file(command: str) -> None:
    part = command.split()
    if len(part) != 3 or part[0] != "mv":
        raise ValueError("Invalid command")
    source = part[1]
    path = part[2]
    path_dir = os.path.dirname(path)
    if path_dir:
        os.makedirs(path_dir, exist_ok=True)
    os.replace(source, path)
