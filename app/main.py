import os


def move_file(command: str):

    with open(command.split()[1], "r") as f:
        content = f.read()
    os.remove(command.split()[1])

    dirs = command.split()[2].split("/")[:-1]
    count = 0
    while count < len(dirs):
        os.mkdir("/".join(dirs[:count + 1]))
        count += 1
    with open(command.split()[2], "w") as f:
        f.write(content)
