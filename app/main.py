import os


def move_file(command: str) -> None:
    files = command.split(" ")
    for i in range(len(files[2].split("/")[:-1])):
        if not os.path.exists("/".join(files[2].split("/")[:i + 1])):
            os.mkdir("/".join(files[2].split("/")[:i + 1]))
    with open(files[2], "w") as f2:
        with open(files[1], "r") as f1:
            f2.write(f1.read())
        os.remove(files[1])
