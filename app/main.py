import os


def move_file(command: str) -> None:
    try:
        command, file, path = command.split()
    except ValueError:
        print("Command should have 2 arguments")
        return

    if command != "mv":
        return

    dirs, target_file = os.path.split(path)

    if dirs:
        try:
            os.makedirs(dirs)
        except FileExistsError:
            pass

    with open(file, "r") as source, open(path, "w") as target:
        target.write(source.read())

    os.remove(file)
