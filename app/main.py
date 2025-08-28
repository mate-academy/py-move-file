import os


def move_file(command: str) -> None:
    commands = command.split()
    arg1 = len(commands) == 3,
    arg2 = commands[0] == "mv",
    arg3 = commands[1][len(commands[1]) - 4:] == ".txt",
    arg4 = commands[2][len(commands[2]) - 4:] == ".txt"

    if (arg1 and arg2 and arg3 and arg4):
        dir_move_file = commands[2].split("/")
        data_file = None
        try:
            with open(commands[1], "r") as file:
                data_file = file.read()
        except FileNotFoundError:
            raise FileNotFoundError
        if len(dir_move_file) > 1:
            os.makedirs("/".join(dir_move_file[:-1]), exist_ok=True)
        with open(commands[2], "w") as move_file:
            move_file.write(data_file)
            os.remove(commands[1])
