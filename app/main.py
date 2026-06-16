import os


def move_file(command: str) -> None:
    command = command.split(" ")
    if "/" in command[2]:
        os.makedirs("/".join(command[2].split("/")[:-1]), exist_ok=True)
    with open(command[2], "w") as f:
        with open(command[1], "r") as o:
            f.write(o.read())
        os.remove(command[1])
