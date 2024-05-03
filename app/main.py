import os


def move_file(command: str) -> None:
    data = command.split()
    if data[0] == "mv" and len(data) == 3:
        if os.path.dirname(os.path.dirname(data[2])):
            os.makedirs(os.path.dirname(data[2]))
        with open(data[1], "r") as r, open(data[2], "w") as f:
            f.write(r.read())
        os.remove(data[1])
