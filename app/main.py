import os


def move_file(command: str) -> None:
    data = command.split()
    if data[0] == "mv" and len(data) == 3:
        dirs = data[2].split("/")
        folder = dirs[0]
        for i in dirs[1::]:
            if not os.path.isdir(folder):
                os.mkdir(folder)
            folder += "/" + i
        with open(data[1], "r") as r, open(data[2], "w") as f:
            f.write(r.read())
        os.remove(data[1])
