import os


def move_file(command: str) -> None:
    split_command = command.split(" ")
    source = split_command[1]
    destination = split_command[2]
    destination = destination.split("/")

    if ".txt" in destination[0]:
        with open(destination[0], "w") as f:
            f.write(open(source).read())
            os.remove(source)
            return

    path = ""
    for i in destination:
        if not os.path.isdir(path + i) and i != destination[-1]:
            path += i + "/"
            os.mkdir(path)
            continue
        if os.path.isdir(path + i):
            path += i + "/"
        if i == destination[-1]:
            path += i
            with open(path, "w") as f:
                f.write(open(source).read())
                os.remove(source)
                return
