import os


def move_file(command: str) -> None:
    try:
        cmd, old_file, path = command.split()
    except ValueError:
        return
    if cmd != "mv":
        return

    make_dir(path)
    with open(old_file, "r") as file, open(path, "w") as new_file:
        new_file.write(file.read())
    os.remove(old_file)


def make_dir(path: str) -> None:
    path = os.path.dirname(path)
    try:
        os.makedirs(path, exist_ok=True)
    except FileNotFoundError:
        pass
