import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) != 3 or command[0] != "mv":
        raise Exception("Wrong command")

    os.makedirs(command[2][:-1], exist_ok=True)
    with open(command[1], "r") as file_in, open(command[2], "w") as file_out:
        file_out.write(file_in.read())
    os.remove(command[1])
