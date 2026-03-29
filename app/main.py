import os


def move_file(commands: str) -> None:
    commands: list = commands.split()
    if commands[0] == "mv" and len(commands) == 3:
        source, destination = commands[1], commands[2]
        path_file = os.path.dirname(destination)
        if path_file:
            os.makedirs(path_file, exist_ok=True)
        os.replace(source, destination)
