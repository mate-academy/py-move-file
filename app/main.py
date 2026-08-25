import os


def move_file(command: str) -> None:
    split_command = command.split(" ")
    if len(split_command) != 3 or split_command[0] != "mv":
        return
    source, destination = split_command[1], split_command[2]
    destination = destination.split("/")
    if destination[-1] == "":
        destination.pop(-1)

    if ".txt" in destination[0]:
        with open(destination[0], "w") as f:
            f.write(open(source).read())
            os.remove(source)
            return

    path = ""
    for i in destination:
        if i == destination[-1] and ".txt" in destination[-1]:
            path = os.path.join(path, i)
            with open(path, "w") as f:
                f.write(open(source).read())
                os.remove(source)
                return
        if i == destination[-1]:
            if not os.path.exists(os.path.join(path, i)):
                path = os.path.join(path, i)
                os.mkdir(path)
            path = os.path.join(path, source)
            with open(path, "w") as f:
                f.write(open(source).read())
                os.remove(source)
                return
        if not os.path.exists(os.path.join(path, i)) and i != destination[-1]:
            path = os.path.join(path, i)
            os.mkdir(path)
            continue
        if os.path.exists(os.path.join(path, i)):
            path = os.path.join(path, i)
