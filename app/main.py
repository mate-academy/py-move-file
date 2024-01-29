import os


def move_file(command: str) -> None:
    commands = command.split()

    if len(commands) == 3 and commands[0] == "mv":
        _, file, path_to_move = commands
        directories, filename = os.path.split(path_to_move)

        if not os.path.isdir(directories) and directories != "":
            os.makedirs(directories, exist_ok=True)

        with open(file, "r") as r, open(path_to_move, "a") as a:
            content = r.read()

            a.write(content)

        os.remove(file)
