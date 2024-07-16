import os


def move_file(command: str) -> None:
    command = command.split(" ")
    # тут 2 if тому шо флейку не подобаэться довжина рядка
    if command[0] == "mv" and len(command) == 3 and os.path.exists(command[1]) and command[0] != command[2]:   # noqa E501
        src = command[1]
        dst = command[2]
        if not os.path.exists(dst):
            create_dirs(dst)
        with open(src, "r") as f1, open(dst, "w") as f2:
            f2.write(f1.read())
        os.remove(src)


def create_dirs(path: str) -> None:
    path = path.split("/")
    if path[-1] != "":
        path = path[:-1]
    print(path)
    temp = ""
    for folder in path:
        if folder != "":
            temp += folder + "/"
            if not os.path.exists(temp):
                os.mkdir(temp)
