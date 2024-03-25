import os


def move_file(command: str) -> None:
    tokens = command.split()
    if len(tokens) == 3 and tokens[0] == "mv":
        cp, source, destination = tokens
        name_dirs = os.path.dirname(destination)

        if name_dirs:
            os.makedirs(name_dirs, exist_ok=True)
        os.replace(source, destination)
