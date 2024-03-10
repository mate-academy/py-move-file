from os import remove, path, makedirs


def move_file(command: str) -> None:
    command = command.split()
    if len(command) != 3 or command[0] != "mv":
        return
    move_to, name = path.split(command[2])
    if move_to:
        makedirs(move_to, exist_ok=True)
    with open(command[1], "r") as file_in, open(command[2], "w") as file_out:
        file_out.write(file_in.read())
    remove(command[1])
