import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        return
    cmd, filename, path_to_file = command.split()

    if cmd == "mv":
        directories = os.path.dirname(path_to_file)
        if directories:
            os.makedirs(directories, exist_ok=True)

        os.replace(filename, path_to_file)
