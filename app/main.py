from os import path, rename, makedirs


def move_file(command: str) -> None:
    args = command.split()

    if (len(args) == 3 and args[0] == "mv" and args[2] != args[1]):
        directory_path = path.dirname(args[2])
        if directory_path:
            makedirs(directory_path, exist_ok=True)
        rename(args[1], "./" + args[2])
