import os


def move_file(command: str) -> None:
    try:
        cmd, file, path = command.split()
    except ValueError:
        print("Command should have 2 arguments")
        return

    if cmd != "mv":
        return

    dirs = "/".join(path.split("/")[:-1])

    if dirs:
        os.makedirs(dirs)

    with open(file, "r") as source, open(path, "w") as target:
        target.write(source.read())

    os.remove(file)


move_file("mv file.txt file2.txt")
