import os


def move_file(command: str) -> str | None:
    cmd = command.split()
    if cmd[0] != "mv":
        return f"{cmd[0]} not a move command"

    path = cmd[2].split("/")
    new_file = path.pop()
    path = "/".join(path)

    if not os.path.isdir(path):
        os.makedirs(path)
    try:
        with open(cmd[1], "r") as source, \
                open(os.path.join(path, new_file), "w") as copy:
            copy.write(source.read())
    except FileNotFoundError:
        return f"{cmd[1]} not found!"

    os.remove(cmd[1])
