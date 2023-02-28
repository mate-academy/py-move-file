import os


def move_file(command: str) -> None:
    command = command.split()
    if command[0] == "mv":
        path_to_new_file = command[2].split("/")
        os.makedirs("/".join(path_to_new_file[:-1]))
    with open(command[1], "r") as of, open(command[2], "a") as nf:
        text = of.read()
        nf.write(text)
    os.remove(command[1])
