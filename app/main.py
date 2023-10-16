from os import path, makedirs, replace


def move_file(command: str) -> None:
    mv_command = command.split()
    if mv_command[0] != "mv" or len(mv_command) != 3:
        return None

    path_file = path.dirname(mv_command[2])
    if path_file:
        makedirs(path_file, exist_ok=True)
    replace(mv_command[1], mv_command[2])
