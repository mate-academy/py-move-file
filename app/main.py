import os


def move_file(command: str) -> None:
    data = command.split()
    if len(data) == 3 and data[0] == "mv" and data[1] != data[2]:
        folders = os.path.dirname(data[2])
        if os.path.dirname(folders):
            os.makedirs(folders)
        with open(data[1], "r") as r, open(data[2], "w") as f:
            f.write(r.read())
        os.remove(data[1])
