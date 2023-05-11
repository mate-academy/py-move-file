import os


def move_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) != 3 or "mv" not in command_split[0]:
        return
    cmd, file_old, path_file = command_split

    if "/" in path_file:
        path, file_name = os.path.split(path_file)
        os.makedirs(path, exist_ok=True)

    with (
        open(file_old, "r") as file_first,
        open(path_file, "w") as file_new
    ):
        file_new.write(file_first.read())
    os.remove(file_old)
