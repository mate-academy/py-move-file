import os


def move_file(command: str) -> None:
    list_command = command.split()
    if len(list_command) != 3 or "mv" not in list_command[0]:
        return
    action, file_old, path_file = list_command
    if "/" in path_file:
        path, file_name = os.path.split(path_file)
        os.makedirs(path, exist_ok=True)
    with open(file_old, "r") as file_first, open(path_file, "w") as file_new:
        file_new.write(file_first.read())
    os.remove(file_old)
