import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        return
    operation, source_file, new_file = command.split()
    if operation != "mv":
        return
    dirs = os.path.dirname(new_file)
    if dirs:
        os.makedirs(dirs, exist_ok=True)

    with open(source_file, "r") as source:
        with open(new_file, "w") as target:
            target.writelines(source.read())

    os.remove(source_file)
