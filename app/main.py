import os


def move_file(command: str) -> None:
    command_args = command.split()
    if len(command_args) != 3 or command_args[0] != "mv":
        raise Exception("Invalid command")
    cmd, file_orig, file_goal = command_args
    path, file = os.path.split(file_goal)
    if not path:
        os.rename(file_orig, file_goal)
        return
    if not file:
        file_goal = os.path.join(file_goal, file_orig)
    os.makedirs(path, exist_ok=True)
    with open(file_orig) as origin_file, open(file_goal, "w") as new_file:
        new_file.write(origin_file.read())
    os.remove(file_orig)
