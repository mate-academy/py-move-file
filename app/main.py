import os


def move_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) == 3 and command_split[0] == "mv":
        comm, file_name, path = command_split

    if "/" not in path:
        os.replace(file_name, path)
        return

    path_without_fn = "/".join(path.split("/")[:-1])
    os.makedirs(path_without_fn, exist_ok=True)
    os.replace(file_name, path)
