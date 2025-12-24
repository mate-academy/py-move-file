import os


def move_file(command: str) -> None:
    commands = command.split()

    if len(commands) == 3 and commands[0] == "mv":
        _, file, path_to_move = commands
        directories, filename = os.path.split(path_to_move)

        if directories:
            os.makedirs(directories, exist_ok=True)

        with (
            open(file, "r") as file_to_move,
            open(path_to_move, "a") as moved_file
        ):
            moved_file.write(file_to_move.read())

        os.remove(file)
