import os


def move_file(command: str) -> None:
    try:
        key, source, target = command.split()
    except ValueError:
        return
    if key != "mv" or source == target:
        return
    if os.path.dirname(target) != "":
        os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(source, "r") as read_file, open(target, "w") as write_file:
        write_file.write(read_file.read())
    os.remove(source)
