import os


def move_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) == 3 and command_split[0] == "mv":
        comm, file_name, path_with_filename = command_split

    if "/" not in path_with_filename:
        os.replace(file_name, path_with_filename)
        return

    path = os.path.split(path_with_filename)
    os.makedirs(path[0], exist_ok=True)
    os.replace(file_name, path_with_filename)
