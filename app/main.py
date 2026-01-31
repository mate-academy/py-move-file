from os import makedirs, remove, rename, path, sep


def move_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) != 3:
        return
    cm, source, dest = command_split
    if cm != "mv":
        return
    if dest.endswith(sep):
        path.join(dest, source)
    if sep not in dest:
        rename(source, dest)
        return
    makedirs(path.join(path.dirname(dest)), exist_ok=True)
    with open(source, "r") as file1, open(dest, "w") as file2:
        file2.write(file1.read())
        remove(source)
