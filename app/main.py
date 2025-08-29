import os


def move_file(command: str) -> None:
    commands = command.split()
    cmd_size = len(commands) == 3
    cmd1 = commands[0] == "mv"
    cmd2 = commands[1][len(commands[1]) - 4:] == ".txt"
    cmd3 = commands[2][len(commands[2]) - 4:] == ".txt"

    if (cmd_size and cmd1 and cmd2 and cmd3):
        dir_move_file = commands[2].split("/")
        data_file = None
        try:
            with open(commands[1], "r") as file:
                data_file = file.read()
        except FileNotFoundError:
            raise FileNotFoundError
        if len(dir_move_file) > 1:
            diretorio = "/".join(dir_move_file[:-1])
            if not os.path.exists(diretorio):
                os.makedirs(diretorio)
        with open(commands[2], "w") as move_file:
            move_file.write(data_file)
            os.remove(commands[1])


