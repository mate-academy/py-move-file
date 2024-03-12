from os import remove, path, makedirs


def move_file(command: str) -> None:
    commands = command.split()
    if len(commands) != 3 or commands[0] != "mv":
        return
    move_to, name = path.split(commands[2])
    if move_to:
        makedirs(move_to, exist_ok=True)
    with open(commands[1], "r") as file_in, open(commands[2], "w") as file_out:
        file_out.write(file_in.read())
    remove(commands[1])
