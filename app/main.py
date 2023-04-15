import os


def move_file(command: str) -> None:
    list_command = command.split()
    if len(list_command) != 3 or "mv" not in list_command[0]:
        return
    action, file_old, path_file = list_command
    os.renames(file_old, path_file)
